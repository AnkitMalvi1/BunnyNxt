import site
from django.contrib import admin
from .models import * 
from django.utils.html import format_html
# from taggit.managers import TaggableManager
# Register your models here.
admin.site.site_header  =  "RINGNXT"  
admin.site.site_title  =  "Manage Ringnxt"
admin.site.index_title  =  "HOME"

# class Intags(admin.TabularInline):
#     model: 

class userAd(admin.ModelAdmin):
    list_display = ['displayName','email','verfiedUser' , 'points']
    search_fields =['email','displayName']
    readonly_fields= ['date_joined','last_login']
    # 'bgmi_id',,'userpoint','dlcheck''verfied_user'
    filter_horizontal= ()
    list_filter =()
    fieldsets= ()
    fieldsets = [
        ['User Info' ,{'fields': ['username','displayName','email','verfiedUser', 'is_superuser', 'is_staff','groups' ,'profile_image' ,'bio']}],
        
        ['Log Info',{'fields':['date_joined','last_login']}],
        ['Social Media',{'fields':['insta','youtube']}],
        ['Coins',{'fields':['points']}],

    ]

class ringtonead(admin.ModelAdmin):
    list_display = ['thumbnail','title','category','user','downloadsformated','publishDate','updateDate'  ]
    search_fields =['title','category','user']
    # readonly_fields= ['user']
    fieldsets = [
        ['Ringtone Info' ,{'fields': ['title','category','user','downloads','played', 'downloadsformated']}],
        ['RIngtone Meta',{'fields':['slug','description', 'duration','tags']}],
        ['File',{'fields':['file','thumb']}],
        ['likes',{'fields':['likes']}],

    

    ]
    prepopulated_fields= {'slug':('title',)}
# thumb
    def thumbnail(self, obj):
        return format_html('<img src="{}" style="border-radius: 5px;width: 50px;height: 50px;object-fit: cover;" />'.format(obj.thumb.url))

class categoryad(admin.ModelAdmin):
    list_display = ['thumbnail','title']
    search_fields =['title']
    # readonly_fields= ['user']
    fieldsets = [
        ['Category Info' ,{'fields': ['name','title']}],
        ['image',{'fields':['image']}],
        ['Category Meta',{'fields':['slug','description']}]
    ]

    prepopulated_fields= {'slug':('name',)}

    def thumbnail(self, obj):
        return format_html('<img src="{}" style="border-radius: 5px;width: 70px;height: 70px;object-fit: cover;" />'.format(obj.image.url))

    

class imagelibadd(admin.ModelAdmin):
    list_display = ['thumbnail','imagecategory']

    def thumbnail(self, obj):
        return format_html('<img src="{}" style="border-radius: 5px;width: 70px;height: 70px;object-fit: cover;" />'.format(obj.image.url))


class suggestedsearchadd(admin.ModelAdmin):
    list_display = ['query','query_count']

     
class Profileadd(admin.ModelAdmin):
    list_display = ['user','name']


class Plansadd(admin.ModelAdmin):
    list_display = ['title','point','rupees','reward_type']
 
   


admin.site.register(Category, categoryad)
admin.site.register(Ringtone, ringtonead)
admin.site.register(User , userAd)
admin.site.register(imagelibrary , imagelibadd)
admin.site.register(suggestedsearch , suggestedsearchadd)
admin.site.register(Profile , Profileadd)
admin.site.register(Plans , Plansadd)
admin.site.register(Payment)



# admin.site.register(ringhit)
 
