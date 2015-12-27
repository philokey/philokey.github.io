Title: caffe & mxnet & fast-rcnn 学习笔记
Date: 2015-12-27
Category: 论文,caffe,mxnet
Tag: CNN


未完成版本。

##背景

CV课的大作业，内容是做物体检测，一开始选择做dog detection，后来顺手又把猫加上了。挣扎了好久，觉得用hog或者其他什么特征是在太过时了，决定用cnn。之前读过rcnn的论文，但是代码是用matlab写的，出于某种偏见，不想读，抑制不住的想要自己实现一个Python版的。

接着是训练工具的选择，首先看了caffe，花了一天半配环境，然后发现不能用Python3，于是吐槽的好久愤然放弃。然后发现mxnet是个好东西，配置方便，文档齐全，跑跑classification的example觉得很开心，支持Python3。但是，用mxnet做detection简直是个噩梦，大概因为是新东西，还没人用来做detection。又冷静思考了一下实现rcnn的工作量，各种零零碎碎的东西加起来，我估计今年过完我都实现不了。所以向现实低头，还是用现成点的东西吧。

回去又看了眼rbg的github，好在ICCV2015上的fast-rcnn不仅又快又好，还是用python写的，还内置了修订版的caffe，于是拜读了代码，觉得人家一个科学家，代码还写这么好，真是不知道比我们高到哪里去了。所以最后的决定是：直接用fast-rcnn + caffe，调整已有的网络，训练猫狗检测模型。

##fast-rcnn论文概述

[论文](http://arxiv.org/pdf/1504.08083v2.pdf)

[Slides](http://tutorial.caffe.berkeleyvision.org/caffe-cvpr15-detection.pdf)

感觉slides读起来很清晰，网络结构说的很清楚。

fast-rcnn是rcnn的升级版，mAP提高了4个点左右，训练速度提高了9倍，测试速度提高了213倍，能做到0.3s一张图。

###整体架构

![整体框架](https://lh3.googleusercontent.com/-hTZgHdAZaZA/Vn9eXkrvzdI/AAAAAAAAG8g/QBt_wR1vvbM/s912-Ic42/%2525E5%2525B1%25258F%2525E5%2525B9%252595%2525E5%2525BF%2525AB%2525E7%252585%2525A7%2525202015-12-27%252520%2525E4%2525B8%25258A%2525E5%25258D%25258811.42.36.png)
网络的整体框架如上图所示，以AlexNet为例。输入分两部分，第一部分是一张原图，先通过5个卷积层，第二部分是selective search生成的2000个ROI，两部分一起通过一个ROIPooling layer，生成长度固定的特征，再进过两个全连接层。作者之前分析了rcnn等方法慢得原因之一是因为采用了pipeline模式，为了加快速度，作者直接搞了连个平行的输出层，也就是说有两个损失函数。一个输出bounding box的predict，用的还是逻辑斯蒂回归，一个输出softmax分类的结果。两个损失函数具体怎么做梯度下降还要再看看源代码吧。

###ROI Pooling layer
ROI Pooling layer是一个特殊的单层的SPP layer，文中的解释没有看的很懂（大概是因为SPP net没读懂）。这一层的作用就是就是把每个ROI变成H*W个grid，然后得到固定大小的feature传入全连接层。
总的来说，还是不太懂作者的意图。

##fast-rcnn代码阅读和修改

###概述

```
├── caffe-fast-rcnn
├── lib
│   ├── datasets
│   ├── fast_rcnn
│   ├── roi_data_layer
│   ├── setup.py
│   └── utils
├── models
│   ├── CaffeNet
│   ├── VGG16
│   └── VGG_CNN_M_1024
└── tools
    ├── _init_paths.py
    ├── compress_net.py
    ├── demo.py
    ├── reval.py
    ├── test_net.py
    ├── train_net.py
    └── train_svms.py
```
fast-rcnn核心代码框架如上所示，其中caffe进过作者的改造，增加了两个层，一个是本文提出的Pooling Layer，另一个是做bounding box回归的Smooth L1 Loss Layer。lib基本包含了论文里面所有的核心代码，modle对应了论文中提到的三个规模的进过pretraining的网络模型，CaffeNet是S，VGG_CNN_M_1024是M，VGG16是L。tools是一些有用的示例代码，在上面改改基本就能训练自己的模型。

###datasets
```
├── datasets
│   ├── __init__.py
│   ├── factory.py
│   ├── imdb.py
│   └── pascal_voc.py```
```
先从输入数据说起。

输入数据的处理在datasets这个模块中完成。imdb.py定义了输入数据的基本类imdb，全称是Image database。使用者可以继承这个类，训练自己的数据，pascal_voc.py给出了很好的例子。调用factory.py里面的函数可以生成和使用imdb。

接下来看要怎么生成自己的输入imdb,其实主要工作量也集中在了处理数据和生成数据上，都是体力活。

比如说我们创建一个新的类，叫做catdog

###roi_data_layer

```
├── roi_data_layer
│   ├── __init__.py
│   ├── layer.py
│   ├── minibatch.py
│   └── roidb.py
```


##用mxnet做图像分类

###概述
看到kaggle上有个cat vs dog的比赛，于是顺手做了个猫狗分类。考虑到用fast-rcnn做分类有点杀鸡用牛刀，而且训练数据并没有标出区域，而且用selective search生成bounding box略麻烦，所以就直接用mxnet来作。

一开始还很naive的想用kaggle给的25000张图的训练数据来做，结果用Alexnet跑了十几个epochs发现validate的准确率还在50%徘徊，然后意识到了数据量的重要新，于是直接上了pretraining好的模型，果然是效果拔群。跑完第一个epoch，准确率是75%，跑完第二个88%，第三个93%，第四个95%。跑到第十几个的时候，训练数据的准确率已经到了99.6%,validate的数据准确率到96.2%，感觉还是有点overfitting了。交到kaggle上，跑出了96.1%的结果，然而第一名的98%多，如果没有pretraining的数据，能跑到那么高么，总之觉得好厉害。

###mxnet使用细节
TO BE UPDATE

##总结
这次project的主要收获


- 学习了两个深度学习的工具，caffe，mxnet。个人很看好mxnet。
- 拜读了Fast R-CNN的部分代码，写的好优雅，思路清晰好读，值得学习。
- 稍微跟进了CV领域比较前沿的论文，虽然因为缺少先验知识，没有特别懂。


