from django.contrib import admin
from settings.models import FAQ, Contact, Info, Money, Products, Settings, Slide, Team, Tiun
# Register your models here.
admin.site.register(Settings)
admin.site.register(Info)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Slide)
admin.site.register(Products)
admin.site.register(Tiun)
admin.site.register(FAQ)
admin.site.register(Money)


