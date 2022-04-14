# lazyTM: 还在为睡过网课而担心吗？

基于pywinauto的定时进入同济courses网课的小工具。


## 如何使用？

1. 安装`conda`
2. 安装下面的依赖
```
pywinauto==0.6.8
PyYAML==6.0
schedule==1.1.0
```
3.  编辑`curriculum.yaml`
```
courses:
  - name: dummy
    cid: 664194332       <---- 会议号
    pwd: 9742            <---- 会议密码
    weekday: thursday    <---- 小写星期
    time: '08:35'        <---- 单引号括起来的时间
  - name: algo
    cid: 688484180
    pwd: 5476
    weekday: thursday
    time: '13:20'
  - name: sj
    cid: 664194332
    pwd: 9742
    weekday: thursday
    time: '18:50'
```
4. 在shell里运行`main.py`，保证电脑不睡眠不锁屏，自己就可以睡大觉了。
   

【目前软体不稳定，炸了请节哀】
## 后续工作
1. [x] 加入读取配置文件功能
2. [ ] 提高鲁棒性，加入异常处理
3. [ ] 。。。
