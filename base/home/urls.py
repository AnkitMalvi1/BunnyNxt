# from atexit import register
from unicodedata import name
from django.urls import path
from .import views  
from django.urls import include, path

from django.urls import re_path
urlpatterns = [
    path('', views.home , name='home'),
    path('upload/', views.user_upload, name='upload'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    
    path('login/', views.userlogin, name='userlogin'),
    path('logout/', views.userlogot, name='userlogot'),
    path('ringtones/', views.ringtones, name='ringtones'),
    path('category/<slug:slug>/',views.category, name="category"),
    path('downloads/mp3/<slug:tag_slug>/',views.tags, name="get_ringtone_by_tag"),

    # re_path('detail/(?<slug>[\w-])+/'
    path('ringtone/<slug:slug>/', views.singleringtone, name='singleringtone'),
    path('incrementUrl/', views.rigntone_incress_download, name='rigntone_incress_download'),
    path('sharecount/', views.rigntone_share, name='rigntone_share'),
    path('ringtonelike/', views.ringtonelike, name='ringtonelike'),
    path('ringtonelikefull/', views.ringtonelikefull, name='ringtonelikefull'),
    path('search_ringtone/', views.search_ringtone, name='search_ringtone'),
    path('suggestedsearch/', views.suggsearch, name='suggsearch'),
    # path('trending/', views.trending, name='trending'),
    path('userprofile/<int:pk>', views.userprofile, name='userprofile'),
    path('redeem/', views.useredeem, name='useredeem'),
    
    path('addfollow/', views.addfollow, name='addfollow'),
    path('ringtone_played/', views.ringtone_played, name='ringtone_played'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('profile_pic_update/', views.profile_pic_update, name='profile_pic_update'),


    
    path('accounts/', include('allauth.urls')),
    

    
    
    


    

    
]