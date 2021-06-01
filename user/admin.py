from django.contrib import admin
from bag.models import bag
from .models import uregister
admin.site.register(uregister)
admin.site.register(bag)
# Register your models here.
