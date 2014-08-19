Title: ubuntu字体
Date: 2014-08-19 12:50
Category: Linux

##基础知识

Sans-serif=无衬线体=黑体：并不是具体一款字体，而是一类字体，选择它其实等于选择这类字体中优先级最高的那款字体。

Serif=衬线体=白体：同上

Monospace=等宽字体，用于终端下面以及编程使用。这类字体的要求是能区分 1 i l，o 0 O。：同上

点阵字体=位图字体

无衬线体更适合电脑屏幕阅读，衬线体适合打印。——因为衬线可以使得人视线平齐于一行。也就是说不会读破行。

中文显示时有不同的方式，一方面因为中文本身拥有的横和同高度就可以导致这种平齐。行距对中文更重要。

##Linux字体

###字体文件存放路径

```
/usr/share/fonts/  #系统字体
~/.fonts #用户字体
```

###配置文件路径

```
/etc/fonts/fonts.conf #系统配置文件,每类字体下的第一种字体优先级最高
~/.fonts.conf #用户配置文件，只对当前用户运行的程序有效
```
###命令

```
fc-cache -fv #通常复制字体进~/.fonts就会自动刷新字体，如果没有，用这个命令，如果复制进的是/usr/share/fonts/，用sudo fc-cache -fv
fc-match sans-serif #抓取当前用户sans-serif类字体优先级最高的那款字体
fc-match serif #抓取当前用户serif类字体优先级最高的那款字体
fc-match monospace #抓取当前用户monospace类字体优先级最高的那款字体
```

