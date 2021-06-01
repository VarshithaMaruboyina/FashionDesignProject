from django.contrib import admin

# Register your models here.
from .models import dregister,designs
admin.site.register(dregister)
admin.site.register(designs)