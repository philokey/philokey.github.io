Title: 论文笔记：Rich feature hierarchies for accurate object detection and semantic segmentation
Date: 2015-12-9
Category: 论文
Tag: CNN
##Object detection with R-CNN

###Module design

先用selective search生成category-independent region proposals，然后从每个region proposal中用CNN提取出4096维的特征向量。
###Test time detection
每张测试图片用selective search 的fast mode大概提取出2000个region proposal. 对每个region，用训练好的CNN提取特征，再用SVM分类，打分。如果region有重叠(IoU)，保留分最高的，舍弃其它。


由于

1. CNN共享参数
2. the feature vectors computed by the CNNare low-dimensional when compared to other common approaches
所以速度比较快。 13s/image on a GPU or 53s/image on a CPU
###Training
用ILSVRC 2012数据集做pre-training，得到粗略的模型,但效果实际上比Alex他们差一点点，作者认为是自己的训练过程比较简单导致的。
微调：将粗略模型的1000分类变成了现在的21分类（20种类+1背景）和ground truth的box重叠超过50%(IoU = 0.5)算正例，否则是负例。
每次mini-batch的size为128，其中32个positive windows，96 backrgound windows。
对positive windows 做 bias
物体种类分类器：region里面有物体的部分，看物体的IoU是否达到阈值，达到才认为是正样本。IoU的设置很重要，这个IoU和上面的不一样，是SVM的，文中设置为0.3，会有好几个百分点的差别。分类用的是hard negative mining svm（然而并不知道这是什么，查查）

###Results on PASCAL VOC 201012

53.3% mAP，比之前的高了10%以上

## Visualization, ablation, and modes of error


###Visualizing learned features
核心思想是在pool5中一个神经元对应回去原图的227 * 227中的195 * 195个像素(术语是pool5神经元的感受野是195 * 195)。这个可以用公式
$$r_i = s_i*(r_(i+1)-1) + k_i$$
其中$r_i$是表示第$i$层layer的输入的区域的大小，$s_i$表示第$i$层layer的stride，$ki_$表示kernel size，注意，不需要考虑padding size。

可视化的方法是将10M的region在训练好的网络中FP，然后看某个pool5中特定的神经元(central pool5 unit)的激活程度并且给一个rank。

###Ablation studies

**Performance layer-by-layer, without fine-tuning** 对没有经过微调，只用PASCAL数据集训练的的网络，用pool5，fc6，fc7的特征做SVM分类，出来的效果都差不多。作者得到的结论是：CNN的特征表达能力大部分是在卷积层。
**Performance layer-by-layer, with fine-tuning** pool5经过finetuning之后，mAP的提高不明显，所以卷积层提取出来的特征是具有普遍性的，而fc7经过finetuning后得到很大的提升，说明finetuning的效果主要是在全连接层上。
**Comparison to recent feature learning methods** 和DPM(Discriminatively trained deformable part models, release 5)方法对比，说明R-CNN的优越性，有更强的学习能力。
###Detection error analysis
一个误差分析工具。把错误分成四类：
1. Loc—poor localization (a detection with an IoU overlap with the correct class between 0.1 and 0.5, or a duplicate);
2. Sim—confusion with a similar category;
3. Oth—confusion with a dissimilar object category;
4. BG—a FP that fired on background.
错误主要是由Loc导致的，加上BB的方法可以有效的减少这类错误
###Bounding box regression
为了解决Loc的问题，在pool5的结构上，用线性回归来进一步定位物体的位置，这样子使得mAP提高了4个点。

##Semantic segmentation

在开源的切分框架O2P上做的

**CNN features for segmentation** 

提出3种策略计算CPMC region的评分

把CPMC regions变成227*227，然后计算特征

策略1(full)：忽略region的形状，直接计算矩形regions上的特征

策略2(fg)：只在region的前景上计算特征

策略3(fg+full)： 把前两个特征合并

