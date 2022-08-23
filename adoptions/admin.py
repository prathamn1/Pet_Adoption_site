from django.contrib import admin

# Register your models here.
from .models import Pet #importing Pet class from models
#to register the below class for with which model it is associated with we will use the decorator

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):  # PetAdmin class which is inheriting from admn.ModelAdmin
    list_display = ['name','sex','species','breed','age',] 
    #list_display is the attribute in the model class which specefies which which items are to be displayed on the screen