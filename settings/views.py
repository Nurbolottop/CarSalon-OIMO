from multiprocessing import context
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from settings.models import FAQ, Info, Money, Products, Settings, Slide,Team,Contact,Tiun
# Create your views here.
#Настройки
def index(request):
    setting = Settings.objects.latest('id')
    slide = Slide.objects.latest('id')
    product = Products.objects.all()
    tiun = Tiun.objects.all()
    moneys = Money.objects.latest('id')


    context={
        'setting': setting,
        'slide': slide,
        'product':product,
        'tiun':tiun,
        'moneys':moneys


    }

    return render(request,'index-shoe.html',context)
#О нас
def about_us(request):
    about = Info.objects.latest('id')
    moneys = Money.objects.latest('id')
    setting = Settings.objects.latest('id')
    teams = Team.objects.all()
    context={
        'about':about,
        'setting': setting,
        'teams' : teams,
        'moneys':moneys

    }

    return render(request,'about-us.html', context)
#Контакты
def contact(request):
    moneys = Money.objects.latest('id')
    setting = Settings.objects.latest('id')
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name = name,email = email,number = phone, subject = subject,message = message)
        send_mail(
            f'{subject}',
            f'{name} Здравствуйте, спасибо за отклик, мы с вами в скором времени свяжемся. Ваше сообщение: {message} Ваши контакты: {email}, {phone}',
            "noreply@somehost.local",
            [email]
        )
        return redirect('index')
    context = {
        'setting': setting,
        'moneys':moneys

    }
    return render (request, 'contact.html', context)
#Продукты
def product_index(request):
    products = Products.objects.all()
    setting = Settings.objects.latest('id')
    moneys = Money.objects.latest('id')

    context={
        'products':products,
        'setting': setting,
        'moneys':moneys
        
    }
    return render(request,'shop.html',context)
#Детали продуктов
def product_details(request,id):
    setting = Settings.objects.latest('id')
    product = Products.objects.get(id = id)
    moneys = Money.objects.latest('id')
   
    
    context={
        'setting': setting,
        'product':product,
        'moneys':moneys
        
    }
    return render(request,'product-2.html',context)
#Блог
def blog(request):
    setting = Settings.objects.latest('id')
    moneys = Money.objects.latest('id')

    context ={
        'setting': setting,
        'moneys':moneys

    }
    return render(request,'blog.html',context)

#Часто задаваемые вопросы
def faq(request):
    setting = Settings.objects.latest('id')
    faqs = FAQ.objects.all()
    moneys = Money.objects.latest('id')

    context ={
        'setting':setting,
        'faqs': faqs,
        'moneys':moneys

    }

    return render (request,'faq.html',context)

#Регистрация    
def register(request):
    setting = Settings.objects.latest('id')
    moneys = Money.objects.latest('id')

    context={
        'setting':setting,
        'moneys':moneys

    }
    return render(request, 'register.html', context)

#Логин 
def login(request):

    setting = Settings.objects.latest('id')
    context = {
        'setting':setting
    }
    return render(request,'login.html', context)

#Список желаний
def wishlist(request):
    setting = Settings.objects.latest('id')

    context = {

        'setting': setting
    }

    return render(request, 'wishlist.html',context)