
from django.shortcuts import render
from settings.models import Info, Products, Settings, Slide,Team,Contact
# Create your views here.
def index(request):
    setting = Settings.objects.latest('id')
    slide = Slide.objects.latest('id')
    product = Products.objects.all()

    context={
        'setting': setting,
        'slide': slide,
        'product':product

    }

    return render(request,'index-shoe.html',context)

def about_us(request):
    about = Info.objects.latest('id')
    setting = Settings.objects.latest('id')
    teams = Team.objects.all()
    context={
        'about':about,
        'setting': setting,
        'teams' : teams,

    }

    return render(request,'about-us.html', context)

def contact(request):
    contacts = Contact.objects.latest('id')
    setting = Settings.objects.latest('id')


    context={
        'setting': setting,
        'contacts': contacts
    }

    return render(request,'contact.html', context)

