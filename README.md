# lazyTM: 还在为睡过网课而担心吗？

基于pywinauto的定时进入同济courses网课的小工具。


## 如何使用？

1. 安装`conda`
2. 安装下面的依赖
```
autopep8==1.6.0
certifi==2020.6.20
comtypes==1.1.11
Jinja2==3.0.3
lxml==4.8.0
MarkupSafe==2.0.1
Pillow==8.4.0
pycodestyle==2.8.0
pygame==2.1.2
PyQt5==5.15.6
PyQt5-Qt5==5.15.2
PyQt5-sip==12.9.1
PySide2==5.15.2.1
python-pptx==0.6.21
pywin32==303
pywinauto==0.6.8
PyYAML==6.0
qt-material==2.7
schedule==1.1.0
shiboken2==5.15.2.1
six==1.16.0
toml==0.10.2
wincertstore==0.2
XlsxWriter==3.0.3
```
3.  编辑`main.py`
```

def job():
    enter_meeting("【这里写会议号】", "【这里写密码】", "【这里写进入会议显示的名称】")

schedule.every().tuesday.at("13:54").do(job) # <---- 这里填课程开始前5min的时间
```
4. 在shell里运行`main.py`，保证电脑不睡眠不锁屏，自己就可以睡大觉了。
   

【目前软体不稳定，炸了请节哀】
## 后续工作
1. [ ] 提高鲁棒性，加入异常处理
2. [ ] 。。。
