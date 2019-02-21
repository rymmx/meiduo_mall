from django.apps import AppConfig


class BooktestConfig(AppConfig):
    name = 'booktest'  # 注册时加载的哪个应用
    verbose_name = "图书管理"
