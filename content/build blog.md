Title: 博客搭建记录
Date: 2014-08-01 21:20
Category: 杂
Tags: Pelican, Blog, Python
厌倦了一次又一次去搜相同问题的答案，写个博客把一些东西记录下来吧。
出于黑客精神，决定自己搭建博客。

Wordpress过于庞大，而且我不会PHP，所以选择了基于python的pelican。
由于github有免费的300M空间，所以博客托管再github上。github还有一个好处就是对markdown的支持不错。

不用数据库，全部都以可见文本形式存储，携带迁移，好开心~

2015.11.29 update

谢天谢地有这篇搭建笔记，重新把博客搭起来并迁移到了Python3，真感人。

##本地配置Pelican

###安装pelican和markdown
    
    pip install pelican
    pip install markdown
    
###启动工程
    pelican-quickstart
目录树如下

    ├── content             #存放.mdn文件
    ├── develop_server.sh   #方便开启测试服务器
    ├── fabfile.py          #配置文件
    ├── Makefile            #方便管理博客的Makefile
    ├── output              #生成的输出文件
    ├── pelicanconf.py      #主配置文件
    └── publishconf.py      #主发布文件，可删除

###尝试写博文
和普通的markdown文件稍有不同，在顶部要有

    Title: My super title
    Date: 2014-08-01 10:20
    Category: Python
    Tags: tag1, tag2
    Slug: my-super-post
    Author: Philokey
    Summary: Short version for index and feeds
前两项必填

###本地运行

在博客根目录下
```
make html
make serve
```
到 http://127.0.0.1:8000/ 可以查看。

###组织文件结构

默认所有都再output里,可以按照日期组织生成的html
在pelicanconf.py里配置:
    
    ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
    ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'


###修改主题

默认主题好丑，可以安装自己喜欢的主题
```
git clone https://github.com/getpelican/pelican-themes.git
cd pelican-themes
sudo pelican-themes -i bootstrap2
```

选择主题，在pelicanconf.py中添加

    THEME = 'bootstrap2'

###安装插件

 ```
 git clone git://github.com/getpelican/pelican-plugins.git
 ```

 以sitemap为例，修改配置文件pelicanconf.py

'''
PLUGIN_PATH = u"pelican-plugins"
PLUGINS = ["sitemap"]
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}
'''

###安装第三方评论系统

在Disqus上申请一个站点，记牢Shortname。 在pelicanconf.py添加

    DISQUS_SITENAME = 'Shortname'

###添加Google Analytics

去Google Analytics申请账号，记下跟踪ID。 在pelicanconf.py添加

    GOOGLE_ANALYTICS = 跟踪ID

听说Google Analytics极其强悍，我没用过，试试吧

至此，本地的部分就差不多搭建完毕了

##使用GitHub Pages

在github上创建一个repository,名字为 username.github.io 并再setting里并再setting里面生成GitHub面生成GitHub Pages，几分钟后，页面会自动生成.

到output里把
```
cd output
git init
git remote add origin git@github.com:username/username.github.io.git
git pull origin master
git add .
git commit
git push origin master 
```
这样在username.github.io里面就可以查看博客

###一键上传
修改Makefile文件

    publish:
    	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
    
    github: publish
    	cd $(OUTPUTDIR) ; git add . ;  git commit -am 'update' ; git push origin master

这样

    make github 
就可以实现一键上传

##申请独立域名

###Godaddy

在[godaddy][1]购买域名，并在Manage My Domains里修改Nameservers为这两个地址：
    
    f1g1ns1.dnspod.net
    f1g1ns2.dnspod.net
使用godaddy自己的DNS服务器会被墙的样子

###Dnspod

在[Dnspod][2]注册账号, 并添加刚申请的域名.
添加到 207.97.227.245 的A记录
并把CNAME的记录值改为 username.github.io.

###Github

在output目录下添加CNAME文件，里面填入
    
    www.申请的域名

这样，博客主题就完成了。其他小功能自己探索吧

##补充

###红框问题
发布之后发现代码里面有奇怪的红框，审查元素得知是css 里面有一个.err的class，如果代码被判断有语法错误就会产生红框，而大部分红框都是误伤。由于每次make html时主题的css都会重新根据安装的主题重新生成一边，所以要先卸载主题

    sudo pelican-themes -i bootstrap2
    
把pygments.css里面的
```
.highlight .err { border: 1px solid #FF0000 } /* Error */
```
去掉

再重新安装主题

  [1]: http://godaddy.com/
  [2]: https://www.dnspod.cn/
