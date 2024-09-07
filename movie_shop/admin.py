from django.contrib import admin
from .models import Category,Janr,Movies
# Register your models here.
admin.site.register(Category)
admin.site.register(Janr)
admin.site.register(Movies)
# admin.site.register(Comments)