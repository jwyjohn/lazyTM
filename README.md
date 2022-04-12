# lazyTM: 还在为睡过网课而担心吗？

基于pywinauto的定时进入同济courses网课的小工具。


## 如何使用？

1. 安装`conda`
2. 安装下面的依赖
```
Pillow==8.4.0
pycodestyle==2.8.0
pywin32==303
pywinauto==0.6.8
PyYAML==6.0
schedule==1.1.0
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
