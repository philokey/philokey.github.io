Date: 2013-08-17
Title: 一步一步打造Geek风格的技术博客
Category: Tech
Tags: pelican, blog, python
Slug: build_blog

##如梦初醒
* * *
###Geek是什么
Geek更多的是一种精神，一种态度，一种对技术的理解与信念。他们无法忍受丑陋的代码，拙劣的技术。他们思路开阔，技术娴熟，他们不甘平庸，追求完美。他们不会囿于常识，他们敢于突破。在常人眼中，他们不走寻常路，享受各种非主流的技术。但在他们自己眼中，这些又是那么得自然与优美。他们用自己的行为诠释着自己对于技术的理解，用那份固执传达着自己的信念。

他们掌握并热爱着技术，叛逆、执着，崇尚自由。

###为什么不选择CSDN、Wordpress、Jekyll等技术
我在CSDN上发表博文被和谐了一次，就不会允许这种事发生第二次。

Wordpress上手容易、功能强大、插件丰富。但是在我看来，这些优点同时也是它的缺点：太笨重、太无脑、不够酷、无用功能太多、可定制的粒度不够小。我更喜欢简洁快速粗暴的博客系统。

Jekyll非常棒，可惜它基于Ruby。对于Python爱好者而言，基于Python的Pelican显然更加可口。

##卧薪尝胆
* * *
我在搭建这个博客的过程中学到了很多很多有意思的技术。

搭建环境为Mac OS X/Linux，Windows下可能会麻烦一些。

搭建过程中会涉及到的技术名词如下：

* Mac OS X
* Python
* Pip
* Pelican
* Jinja2
* Github 
* Git
* Makefile
* Markdown
* Mou
* Google Analytics
* Google Custom Search
* Google Webmasters
* Picasa
* Disqus
* Rss
* Sitemap
* Godaddy
* Dnspod
* A记录

若对任何一个技术名词有疑问，请翻墙[Google](https://www.google.com/ncr) it.

##初见端倪
* * *
开始动手。
###Github入门指南
请参考<http://blog.csdn.net/duxinfeng2010/article/details/8654690>

###使用Github Pages创建个人博客
Github为每一个用户分配了一个二级域名username.github.io，用户为自己的二级域名创建主页很简单，只需要在Github下创建一个名为username.github.io的版本库，并向其master分支提交网站静态页面即可。

* 登陆Github，创建一个名为username.github.io的版本库（将username替换成自己的Github账户名）。
* 点击Setting，选择一个自己喜欢的模板，最后点击发布public按钮。
* 耐心等待一段时间（不超过10分钟），登陆http://username.github.io，会发现自己的个人博客已经生成。

###安装Pelican和Markdown
    pip install pelican
    pip install markdown

###搭建骨架
    mkdir blog
    cd blog
    pelican-quickstart

根据提示一步步输入相应的配置项，不知道如何设置的接受默认即可，后续可以通过编辑pelicanconf.py文件更改配置)

以下是生成的目录结构：
    
    blog/
    ├── content              # 存放输入的源文件
    │   └── (pages)          # 存放手工创建的静态页面
    ├── output               # 生成的输出文件
    ├── develop_server.sh    # 方便开启测试服务器
    ├── Makefile             # 方便管理博客的Makefile
    ├── pelicanconf.py       # 主配置文件
    └── publishconf.py       # 主发布文件，可删除

进入output把自己刚刚建好的username.github.io版本库clone下来：
    
    cd output
    git clone git@github.com:username/username.github.io.git
    
###开始写博文
在content目录下用Markdown语法来写一篇文章，最好选择专业的Markdown编辑器，在Mac OS X下推荐使用Mou，在Linux/Windows下请Google。

用Markdown写博文截图如下：
![1](https://lh5.googleusercontent.com/-edzDa6ch3Jk/Ug5oATNTjsI/AAAAAAAAAKs/WIqU7KziyOA/w958-h599-no/%25E5%25B1%258F%25E5%25B9%2595%25E5%25BF%25AB%25E7%2585%25A7+2013-08-17+%25E4%25B8%258A%25E5%258D%25881.57.09.png)

左半边是正在用markdown写的博文，右边是即时预览效果。

写完后，执行以下命令，即可在本机<http://127.0.0.1:8000>看到效果。

    make publish
    make serve

若要一键上传到Github，需要修改Makefile两处地方：
    
    publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
    
    github: publish
	cd OUTPUTDIR ; git add . ;  git commit -am 'your comments' ; git push

以后写完文章执行make github就可以一键部署了。

##如虎添翼
* * *
我们已经能成功地用markdown写出博文并部署到github了，但这远远不够。

###管理图片
我觉得使用云相册比本地图片要方便的多，我使用[Picasa](https://picasaweb.google.com?noredirect=1)来维护blog的所有图片。

###挑选主题
安装主题，比如bootstrap2：

    git clone https://github.com/getpelican/pelican-themes.git
    cd pelican-themes
    pelican-themes -i bootstrap2

选择主题，在pelicanconf.py中添加
    
    THEME = 'bootstrap2'

###安装第三方评论系统
在[Disqus](https://disqus.com/admin/signup)上申请一个站点，记牢Shortname。
在pelicanconf.py添加
    
    DISQUS_SITENAME = Shortname

 
###添加Google Analytics
去[Google Analytics](http://www.google.com/analytics)申请账号，记下跟踪ID。
在pelicanconf.py添加
    
    GOOGLE_ANALYTICS = 跟踪ID

Google Analytics极其强悍，截图说明一切：
![2](https://lh6.googleusercontent.com/-9vXmIT6vXDo/Ug5wTSu4wMI/AAAAAAAAALM/5-VSrnXNGUU/w958-h599-no/%25E5%25B1%258F%25E5%25B9%2595%25E5%25BF%25AB%25E7%2585%25A7+2013-08-17+%25E4%25B8%258A%25E5%258D%25882.31.26.png)

![3](https://lh6.googleusercontent.com/-a4ZAnTD7F0I/Ug5wTX0w9nI/AAAAAAAAALI/x9J0atK3lpU/w958-h599-no/%25E5%25B1%258F%25E5%25B9%2595%25E5%25BF%25AB%25E7%2585%25A7+2013-08-17+%25E4%25B8%258A%25E5%258D%25882.31.54.png)

###使用Google Webmasters
在[Google Webmasters](http://www.google.com/webmasters)上注册即可。

这个就是Google站长工具，使用它的目的是为了让博客被Google更好的收录，比如手动让Googlebot抓取、提交Robots、更新Sitemap等等，各方面完爆百度站长工具。

截图如下：
![3](https://lh3.googleusercontent.com/-tYrEbXyx_5o/UhGS1C_lcYI/AAAAAAAAALk/H7X7MBjNkVY/w958-h599-no/%25E5%25B1%258F%25E5%25B9%2595%25E5%25BF%25AB%25E7%2585%25A7+2013-08-19+%25E4%25B8%258A%25E5%258D%258811.36.32.png)

###添加插件
    git clone git://github.com/getpelican/pelican-plugins.git
比如我要使用sitemap，在pelicanconf.py里配置如下
    
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

###使用Google站内搜索
请参考<http://www.codenut.net/post/2013-06-30-cse>

###申请独立域名
* 在[Godaddy](https://www.godaddy.com)上用支付宝花购买为期一年的顶级域名，并去修改Nameservers为这两个地址：f1g1ns1.dnspod.net、f1g1ns2.dnspod.net。
* 在[Dnspod](https://www.dnspod.cn)上添加新域名，并申请一条A记录指向Github Pages的ip:207.97.227.245；
* 在Pelican主目录新建CNAME文件，添上刚刚申请的域名，如我的www.lizherui.com

##登峰造极
* * *
最后，如果感觉还不够味儿，可以参考Pelican官方文档和这个博客的完整源码。

Pelican : <http://docs.getpelican.com/en/3.2>

Source Code : <https://github.com/lizherui/lizherui.github.io> 

Have fun!






