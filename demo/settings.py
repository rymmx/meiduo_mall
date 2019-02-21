"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# 导入包(os 路径拼接)
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 项目根路径  /home/python/Desktop/meiduo_mall/demo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Django为我们提供的密钥,如果后期有功能需要进行为密可以用此密钥
SECRET_KEY = 'f+p#kunpl_f^y20cyvxo!1can-tipmlm)q(nrvank-r#4%hff+'

# SECURITY WARNING: don't run with debug turned on in production!
# Django项目默认就开启调试模式,将来项目开发完成部署上线时,需要把DEBUG改False
# 如果将DEBUG改为False我们的Django服务器不会再对静态文件提供访问的能力,因为Django它是一个动态业务逻辑服务器,
# 它更擅长动态业务逻辑处理,不擅长静态文件访问  将来项目部署把项目中的静态文件放在 nginx
DEBUG = True

# 允许那此host访问Django后端
ALLOWED_HOSTS = []


# Application definition
# 安装 注册应用(原生/第三方  子应用)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # 默认开启了session
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users.apps.UsersConfig',  # 注册子应用
    'request_response.apps.RequestResponseConfig',  # 演示请求和响应子应用
    'booktest.apps.BooktestConfig',  # 注册booktest应用
    # 如果视图中只有视图路由这些业务逻辑,子应用可以注册,也可以不注册
    # 如果子应用中使用了模型并且要做迁移建表,如果子应用中应用了模板,一般也要注册
]

# 中间件类似于请求勾子(监听请求和响应的中间过程)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # 默认开启了session
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 中间件的执行原理,请求是自上而下,响应是自下而上
    'users.middleware.my_middleware',  # 添加自定义中间件
    'users.middleware.my_middleware2',  # 添加自定义中间件
]

# 工程路由入口
ROOT_URLCONF = 'demo.urls'

# 项目模板配置项目  /home/python/Desktop/meiduo_mall/demo/templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 项目上线后服务启动文件入口
WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# 数据库的配置
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库后端引擎
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': '3306',  # 数据库端口
        'USER': 'root',  # 用户名
        'PASSWORD': '123456',  # 密码
        'NAME': 'django_demo_23'  # 数据库名字
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
# 密码认证配置
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# 语言本地化配置项 默认是英语,可以改成简体中文  'zh-Hans'
LANGUAGE_CODE = 'zh-Hans'
# LANGUAGE_CODE = 'en-us'

# 本地化时区配置项: 默认是世界时区,可以改成上海时区  'Asia/Shanghai'
TIME_ZONE = 'Asia/Shanghai'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# 配置项目中静态文件存放/读取目录
STATICFILES_DIRS = [
    # http://127.0.0.1:8000/static/index.html
    # http://127.0.0.1:8000/static/mm03.jpg
    os.path.join(BASE_DIR, 'static_files'),
    os.path.join(BASE_DIR, 'static_files/good'),
]
# print("静态文件入口: ",STATICFILES_DIRS)


# 配置session缓存的后端
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# 指定上传文件目录
MEDIA_ROOT=os.path.join(BASE_DIR,"static_files/media")