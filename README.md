# Django-shop
用python Django做的订单后台管理系统，支持开源，欢迎使用，这是我上传的第一个GitHub项目，还希望大家帮帮忙点亮Star，谢谢啦！
这是我的CSDN博客，欢迎私信，留言等 https://blog.csdn.net/weixin_43648017

# 实现功能
 - 用户登录注册，退出账号，修改密码等
 - 新注册用户直接保存到数据库，属于普通用户，管理者为超级用户
 - 首页由数据库渲染，增删查改也是修改数据库内容，数据库采用sqlite3
 - 已注册过的用户名不能再注册，同时密码不正确无法登录
 - 商品信息，顾客信息进行增删查改，并保存到数据库sqlite3
 - 首页图片轮播效果
 
 # 开发技术
 - python  Django
 - Boostrap4
 - sqlite3
 
 # 软件 
 - PyCharm
 
 # 代码使用方法
 - 打开PyCharm
 - 配置相应的环境
 - 打开Terminal终端，输入 python manage.py runserver
 - 点击执行后的链接 进入login页面 `http://127.0.0.1:8000/loginpage/`
 - 注册新用户,即可使用  
 
 # 新建超级管理员方法（即后台管理者，权限最大）
 - Terminal 终端输入以下代码 python manage.py createsuperuser
 - 用户名随便起  邮箱随便起（能记住就行） 密码不会显示出来，要设置，你放心敲就行，它存在，只是不显示 ，然后回车
 - 超级管理员新建成功
 - 终端输入 python manage.py runserver
 - 用刚刚注册的超级管理员登录  `http://127.0.0.1:8000/admin/`
 - 后台数据就可以看到了
 
 # 关闭 python manage.py runserver 的方法
 CTRL + C 即可关闭程序执行
 
 
 # 图片展示
![](https://img-blog.csdnimg.cn/20200804175553831.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzY0ODAxNw==,size_16,color_FFFFFF,t_70)
![](https://img-blog.csdnimg.cn/20200804175606755.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzY0ODAxNw==,size_16,color_FFFFFF,t_70)
![](https://img-blog.csdnimg.cn/20200804175409164.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzY0ODAxNw==,size_16,color_FFFFFF,t_70)
![](https://img-blog.csdnimg.cn/20200804175432710.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzY0ODAxNw==,size_16,color_FFFFFF,t_70)
![](https://img-blog.csdnimg.cn/20200804175443715.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzY0ODAxNw==,size_16,color_FFFFFF,t_70)
![](https://img-blog.csdnimg.cn/20200804175501174.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzY0ODAxNw==,size_16,color_FFFFFF,t_70)
![](https://img-blog.csdnimg.cn/20200804175521877.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzY0ODAxNw==,size_16,color_FFFFFF,t_70)
![](https://img-blog.csdnimg.cn/20200804175537206.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzY0ODAxNw==,size_16,color_FFFFFF,t_70)

