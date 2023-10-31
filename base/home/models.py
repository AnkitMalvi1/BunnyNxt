# from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from operator import mod
import profile
from telnetlib import STATUS
 
from django.db import models
from hitcount.models import HitCount
from hitcount.models import HitCountMixin
# Create your models here.
from .manager import UserManager
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# from slugify import slugify
from mutagen.mp3 import MP3
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from treebeard.mp_tree import MP_Node

from numerize import numerize
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.
class User(AbstractUser):
    username = models.CharField(max_length=150, default="user")
    displayName = models.CharField(max_length=150)
    email = models.EmailField(max_length=50,null=True ,blank=True ,unique=True )
    verfiedUser = models.BooleanField(null=True)
    profile_image = models.ImageField(upload_to='profile/' , default="media\bn.png")
    bio = models.TextField(max_length=150)
    insta = models.URLField(max_length=150 ,default="https://www.instagram.com/_dhirz/") 
    youtube = models.URLField(max_length=150, default="https://www.instagram.com/_dhirz/") 
    points = models.IntegerField(default=0)
    paytm_num = models.CharField(max_length=20, default=0)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

p_Type = (
    ("redeem", "redeem"),
    ("cash", "cash"),
    
)
p_status = (
    ("1", "in Review"),
    ("2", "Success"),
    
)

class Payment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_number =  models.CharField(max_length=140 , default=1)
    inr = models.IntegerField(default=1)

    payment_type  =  models.CharField(
    max_length = 20,
    choices = p_Type,
    default = 'No'
    )

    status = models.CharField(
        max_length = 20,
        choices = p_status,
        default = 'in Review'
        )

    def __str__(self):
        return str(self.user.displayName)

    
 
    


class Category(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)   
    description =  models.TextField(max_length=250)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='cat_images/')

    def __str__(self):
        return str(self.name)
    def get_absolute_url(self):
        return reverse('category', kwargs={'slug':self.slug})
    # catlogo  = models.ImageField(upload_to='cat_images_logo/',  default='username/user.png')

 
    @property
    def get_products(self):
        return Ringtone.objects.filter(category__title=self.title).order_by('-played')[:5]

class Ringtone(models.Model , HitCountMixin):
    title = models.CharField(max_length=150)
    description =  models.TextField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    file = models.FileField(upload_to='urls/')
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    slug = models.SlugField(null=False, unique=True, allow_unicode=True)
    publishDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    downloads = models.PositiveIntegerField(default=0)
    duration = models.PositiveIntegerField(default=0)
    thumb = models.ImageField(upload_to='ringtonesimage/')
    played = models.PositiveIntegerField(default=0)
    share = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='ringtone_like')
    downloadsformated = models.CharField(max_length=120, default="0")
    new_text =models.TextField(max_length=250 , default="NO")
    hitcounts = GenericRelation(
        HitCount,
        content_type_field='content_type',
        object_id_field='object_pk',
    )
    


    def number_of_likes(self):
        return self.likes.count()

    tags = TaggableManager()



    

    def __str__(self):
        return str(self.title)
    
    

    def save(self,*args, **kwargs):
      
        
        value = numerize.numerize(self.downloads)
        self.downloadsformated = value 
        audio = MP3(self.file)
        audio_info = audio.info    
        length_in_secs = int(audio_info.length)
     

      
        self.duration = length_in_secs


        
       
        super(Ringtone, self).save(*args, **kwargs)
 
         

    def get_absolute_url(self):
        return reverse('singleringtone', kwargs={'slug':self.slug})

 

class imagelibrary(models.Model):
    imagecategory = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='ringtoneimage/')

class suggestedsearch(models.Model):
    query = models.CharField(max_length=150)
    query_count = models.PositiveIntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User ,primary_key=True, verbose_name='User',related_name='profile', on_delete=models.CASCADE)
    name  = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True ,null=True)
    profile_pic = models.ImageField(upload_to='profileimages/')
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    following = models.ManyToManyField(User, blank=True, related_name='following')

    def followers_of(self):
        return self.followers.count()
     
    def following_of(self):
        return self.following.count()


@receiver(post_save ,sender=User )
def create_user_profile(sender,instance , created, **kwargs):
    if created:
        # self.slug = self.slug.split(" ","") )

        Profile.objects.create(user=instance)

@receiver(post_save ,sender=User)
def save_user_profile(sender, instance , **kwargs):

    instance.profile.save()





# Reward System


# class Points(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
#     plans = 0

Reward_Type = (
    ("Paytm", "Paytm"),
    ("Points", "Points"),
    
)


class Plans(models.Model):
    
    title = models.CharField(max_length=50)
    point = models.IntegerField(default=0 , blank=True, null=True)
    rupees = models.IntegerField(default=0 , blank=True, null=True)
    # rupees_point = models.IntegerField(default=0 , blank=True, null=True)
    # rupees_point_cent = models.IntegerField(default=0 , blank=True, null=True)
    reward_type = models.CharField(
        max_length = 20,
        choices = Reward_Type,
        default = 'No'
        )
    # rewardcheck = models.BooleanField(null=True , default=False) 
    
    

    def __str__(self):
        return self.title


    def save(self,*args, **kwargs):


        value  = self.point * 5/100
        
        self.rupees = value

        
       
        super(Plans, self).save(*args, **kwargs)