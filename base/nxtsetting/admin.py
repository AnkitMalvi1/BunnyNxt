from django.contrib import admin
from .models import * 
# Register your models here.

class Homead(admin.ModelAdmin):
    list_display = ['name']
    # readonly_fields= ['user']
    fieldsets = [
        ['Home Setting' ,{'fields': ['title','name','separator','description']}],
        
    ]
class Catad(admin.ModelAdmin):
    list_display = ['name']
    # readonly_fields= ['user']
    fieldsets = [
        ['Category Setting' ,{'fields': ['name','description']}],
      
    ]


class Ringtonead(admin.ModelAdmin):
    list_display = ['name']
    # readonly_fields= ['user']
    fieldsets = [
        ['Category Setting' ,{'fields': ['name','description']}]
        
    ]








admin.site.register(Home, Homead)
admin.site.register(Ring, Ringtonead)
admin.site.register(Cat, Catad)