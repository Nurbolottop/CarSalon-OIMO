"""OIMO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from settings.views import about_us, faq, index, login, product_details, product_index,blog,contact, register, wishlist
from django.conf.urls.static import static  
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

#Настройки
    path('',index, name = 'index'),         

#О нас
    path('about-us/',about_us, name = 'about_use'),

#Команда
    path('teams/',about_us , name  = 'team_name'),

#Настройка продуктов
    path('product/',index , name  = 'product'),

#ТЮН 
    path('tiun/',index , name  = 'tiun'),

#Продукты
    path('products/', product_index, name = 'products'),

#Деталь Продуктов
    path('products/<int:id>', product_details, name = 'product_detail'),

#Блог
    path('blogs/', blog, name = 'blogs'),

#Часто задаваемые вопросы
    path('faqs/', faq, name = 'faqs'),

#Контакты
    path('contacts/',contact, name = "contacts"),

#Регистрация
    path('register/',register,name = "register"),


#Логин
    path('login/',login, name = "login"),


#Список желаний
    path("wishlist/",wishlist, name="wishlist")
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 