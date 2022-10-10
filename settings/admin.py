from telnetlib import SE
from django.contrib import admin
from settings.models import Contact, Info, Products, Settings, Slide, Team
# Register your models here.
admin.site.register(Settings)
admin.site.register(Info)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Slide)
admin.site.register(Products)

