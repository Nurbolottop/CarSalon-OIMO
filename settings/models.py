
from statistics import mode
from django.db import models

# Create your models here.
class Settings(models.Model):
    logo_site = models.ImageField(upload_to = 'logo_site/')
    name_site = models.CharField(max_length = 255)
    descriptions_site = models.CharField(max_length =255)
    number_site = models.CharField(max_length = 255)
    twitter_site = models.URLField()
    facebook_site = models.URLField()
    instagram_site =models.URLField()
    tiktok_site =models.URLField()
    youtube_site = models.URLField()

    class Meta:
        verbose_name_plural = "Настройка"
        verbose_name = "Настройки"

    def __str__(self):
        return self.name_site

class Info(models.Model):
    logo_s = models.ImageField(upload_to = 'logo_site/')
    about_s = models.CharField(max_length = 255)
    desc_s =  models.CharField(max_length = 255)

#Пункт 1
    about_1 = models.CharField(max_length = 255)
    desc_1 = models.CharField(max_length = 255)
#Пункт 2
    about_2 = models.CharField(max_length = 255)
    desc_2 = models.CharField(max_length = 255)
#Пункт 3
    about_3 = models.CharField(max_length = 255)
    desc_3 = models.CharField(max_length = 255)

# Дополнительно 1
    dop_photo_1 = models.ImageField(upload_to = 'logo_site/')
    dop_name_1 =models.CharField(max_length = 255)
    dop_desc_1 =models.CharField(max_length = 255)

#Дополнительно 2
    dop_photo_2 = models.ImageField(upload_to = 'logo_site/')
    dop_name_2 =models.CharField(max_length = 255)
    dop_desc_2 =models.CharField(max_length = 255)

#Дополнительно 3
    dop_photo_3 = models.ImageField(upload_to = 'logo_site/')
    dop_name_3 =models.CharField(max_length = 255)
    dop_desc_3 =models.CharField(max_length = 255)



    class Meta:
        verbose_name_plural = "О нас"
        verbose_name = "О нас"

    def __str__(self):
        return self.about_s

class Team(models.Model):
    photo =models.ImageField('team_image/')
    name_and_surname = models.CharField(max_length = 255)
    job = models.CharField(max_length = 255)


    def __str__(self):
        return self.name_and_surname

    class Meta:
        verbose_name_plural = "Сотрудник"
        verbose_name = "Сотрудники"
class Contact(models.Model):
    email_con1 = models.EmailField()
    email_con2 = models.EmailField()
    location_site = models.CharField(max_length = 255)
    phone_number_1 =models.CharField(max_length = 255)
    phone_number_2 =models.CharField(max_length = 255)
    def __str__(self):
        return self.phone_number_1

    class Meta:
        verbose_name_plural = "Контакты"
        verbose_name = "Контакты"

class Slide(models.Model):
#Слайд -1
    slide_photo1 =models.ImageField('slide_photo/') 
    slide_name1 = models.CharField(max_length = 255)
    slide_desc1 = models.CharField(max_length = 255)
#Слайд -2 
    slide_photo2 =models.ImageField('slide_photo/') 
    slide_name2 = models.CharField(max_length = 255)
    slide_desc2 = models.CharField(max_length = 255)
# Слайд 3
    slide_photo3 =models.ImageField('slide_photo/') 
    slide_name3 = models.CharField(max_length = 255)
    slide_desc3 = models.CharField(max_length = 255)

    def __str__(self):
        return self.slide_name1

    class Meta:
        verbose_name_plural = "Слайд"
        verbose_name = "Слайды"

class Products(models.Model):
    pro_photo = models.ImageField('product_photo/') 
    pro_name = models.CharField(max_length =255)
    pro_price = models.CharField(max_length=255)
    pro_price_rebate = models.CharField(max_length = 255)

    def __str__(self):
        return self.pro_name

    class Meta:
        verbose_name_plural = "Продукт"
        verbose_name = "Продукты"