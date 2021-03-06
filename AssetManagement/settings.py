"""
Django settings for AssetManagement project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import time

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-36g_kab12k_u*fxq_avg!b#qgm^-tz30_nz)nzbt$y)vq)l!l0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'asset',
    'tools',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AssetManagement.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'AssetManagement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'AssertManagement',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '192.168.137.134',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

#以下是SIMPLEUI设置
# admin后台登录后的默认地址
LOGIN_REDIRECT_URL = '/'
# 设置后台文本为中文
LANGUAGE_CODE = 'zh-hans'
# 设置后台时区
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False  # 这里务必调整为False，否则时区设置无效

#关闭帮助simpleui改进的统计分析信息
#SIMPLEUI_ANALYSIS = False

SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_QUICK = False
SIMPLEUI_HOME_ACTION = False
SIMPLEUI_ANALYSIS = False

SIMPLEUI_CONFIG = {
    'system_keep': False,     # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': True,    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [{
                'name': '用户',
                'icon': 'fa fa-user',
                'url': 'auth/user/'
            }]
        },
        {
            'app': 'asset',
            'name': '资产管理',
            'icon': 'icon fas fa-tags',
            'models': 
            [{
                'name': '主机资产',
                'icon': 'fa fa-list',
                'url': 'asset/host_assets'
            },
            {
                'name': 'web资产',
                'icon': 'fa fa-list',
                'url': 'asset/web_assets'
            },
            {
                'name': '批量导入数据',
                'icon': 'fa fa-list',
                'url': 'https://www.baidu.com'
            }]
        },
        {
            'app': 'tools',
            'name': '小工具',
            'icon': 'fas fa-user-shield',
            'models': [{
                'name': 'txt去重',
                'icon': 'fa fa-user',
                'url': 'tools/removesame/'
            },]
        },
    ]
}

