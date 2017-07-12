#  search not only for pygame 
http://nullege.com/


# 独立游戏大赛
https://www.indienova.com/indieplay/index
http://cnews.chinadaily.com.cn/2017-05/27/content_29524380.htm


# 指导思想
使用sqlite存储已有信息，与新的对象对应 
考虑使用OOP+TDD方式开发
原数据文件通过解析转换程序将数据导入sqlite

# 文件说明
parse.py 解析TIMES文档到sqlite3

# 资料收集
## [传说中蝈蝈大人的网盘](http://155700.ys168.com/)
http://155700.ys168.com/
##  下载（原版+猛将传）
https://pan.baidu.com/share/home?uk=1544006096#category/type=0
##  修改工具与说明
http://mubiao666.ys168.com/
##  shp文件处理
http://tieba.baidu.com/p/977576485
##  pak文件处理
https://github.com/Tarik02/pak/blob/master/pak/PAK.cs


# 开发指南
使用tk开发GUI
http://effbot.org/tkinterbook/

使用dataset存储标准化数据
https://dataset.readthedocs.io/en/latest/quickstart.html#connecting-to-a-database


# 其他

### take color
tk不能获取窗口外事件
- pywin32获取屏幕事件
- pil获取颜色
- tk做界面
```python
from tkinter import *

root = Tk()

root['height'] = 300                     #设置高
root['width'] = 500                      #设置宽
root.title('魔方小站')                    #设置标题
root['bg'] = '#0099ff'                   #设置背景色
root.geometry('500x300')                 #设置窗口大小  是x不是*
root.geometry("500x300+120+100")         #设置窗口大小  并初始化桌面位置
root.resizable(width=False,height=True)  #宽不可变 高可变  默认True
root.minsize(300,600)                    #窗口可调整的最小值
root.maxsize(600,1200)                   #窗口可调整的最大值
root.attributes("-toolwindow", 1)        #工具栏样式
root.attributes("-topmost", -1)          #置顶窗口
root.state("zoomed")                     #窗口最大化
root.iconify()                           #窗口最小化
root.attributes("-alpha",1)              #窗口透明化 透明度从0-1，1是不透明，0是全透明
root.iconbitmap('c:\\logo.ico')          #设置左上角图标


root.mainloop()

```

tk和pyHook的事件监听冲突
http://stackoverflow.com/questions/37909484/tkinter-text-entry-with-pyhook-hangs-gui-window/37918874#37918874

>使用背景透明法搞定
```text
root.attributes("-alpha",1)
```

### novel

### cocos2d
```python
# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
```
##### 使用帧动画
http://blog.csdn.net/ssihc0/article/details/7698790

### cocos场景黑
gl设默认color
glClearColor

### cocos黑背景精灵
使用shader去除

alpha blending 混合ab的rgb像素，用于制作透明效果




### 3D阴影效果

https://github.com/wagerfield/flat-surface-shader

[demo](http://matthew.wagerfield.com/flat-surface-shader/)