## 推荐使用pycharm专业版操作，python3.10

### 项目文件结构
```
.
|-- CarmiSystem
|   |-- __init__.py
|   |-- __pycache__
|   |-- asgi.py		# ASGI配置文件，用于配置异步服务器的接口
|   |-- settings.py		# 项目的全局配置文件 
|   |-- urls.py		# URL路由配置文件，定义了URL与视图的映射关系
|   `-- wsgi.py		# WSGI配置文件，用于配置与Web服务器
|-- README.md	# 项目说明文件
|-- carmisystemnginx.conf	# 用于配置Nginx服务器与Django项目的连接和部署
|-- ext		#存储重新类拓展和自定义功能
|   |-- __init__.py
|   |-- __pycache__
|   |-- auth.py		#身份认证
|   |-- code.py		#响应码
|   |-- djangofilters.py	#条件筛选器
|   |-- hook.py		#自定义钩子函数
|   |-- paginations.py	#分页器
|   |-- per.py		#权限认证
|   |-- serializers.py	#序列化器
|   |-- throttle.py	#限流器
|   `-- view.py		#自定义视图类
|-- manage.py	# Django项目管理文件
|-- requirements.txt	#项目依赖包
|-- run.sh		#uwsgi和nginx启动
|-- static		#静态文件存储位置
|-- uwsgi.ini		#uwsgi配置文件
`-- web
    |-- __init__.py
    |-- __pycache__
    |-- admin.py	# 管理后台中注册的模型类
    |-- apps.py		# 配置应用程序的文件
    |-- migrations	#数据表迁移文件
    |-- models.py	#数据表文件
    |-- tests.py		#测试文件
    `-- views.py	#app视图

```

1. 直接克隆整个项目，不要使用拉取。（文件夹名字必须是CarmiSystem，然后里面也有一个文件夹叫CarmiSystem）
2. 用pycharm打开CarmiSystem文件夹项目（注意要使用DJango模式打开）
3. 自己创建一个独立venv环境，进入venv环境，进入\venv\Scripts\文件夹，直接运行activate文件 
4. 修改setting.py里面的参数还有view的redis配置
5. 安装python需要的依赖包 
   - 在项目文件目录（根目录）
   - ```pip install -r requirements.txt```
5. 需要提前安装MySQL，需要修改setting.py关于databases的数据（若使用默认数据库，会生成一个数据库在根目录）
   - 先修改一些MySQL的参数，让他与你电脑的参数一致，不然无法连接数据库
   - 安装mysql模块：```pip install mysqlclient```
   - 手动创建数据库
   - 简单理解：每次修改了配置和数据库模块都要执行下面两行
   - makemigrations，读取已经注册所有的app中的models.py文件，根据类生成配置文件并放到app下的migrations目录
   - ```python manage.py makemigrations```
   - migrate，根据配置文件自动生成相应的SQL语句。
   - ```python manage.py migrate```
6. 运行项目，在创建的python环境运行，如果前面配置好了直接点绿色箭头就不需要终端执行代码
   - 注意进入自己的环境，然后终端执行代码：```python manage.py runserver```