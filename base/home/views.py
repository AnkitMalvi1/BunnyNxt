from asyncio import sleep
# from distutils.log import error
import email
from http.client import OK, HTTPResponse
from logging import exception
from msilib.schema import Error
from this import s
from django.shortcuts import HttpResponse
from traceback import print_tb
from django.utils import timezone
import datetime 
from email.mime import image
import json
from os import remove
import random
from turtle import title
from unicodedata import category
from venv import create
from webbrowser import get
from .models import Category, Profile, User, Ringtone, imagelibrary , suggestedsearch , Payment ,Plans
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from slugify import slugify
from nanoid import generate
from validate_email import validate_email
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as userlogout
from django.contrib.auth.decorators import login_required
from mutagen.mp3 import MP3
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
 
import uuid
from django.core import paginator
from django.template.loader import render_to_string
from django.db import models

from nxtsetting .models import*

 
# from tagging.models import Tag
def home(request):
    return render(request, "index.html")

@csrf_exempt
def user_upload(request):
    if request.method == 'POST':
        # ==============================
        current_user = request.user
        myuser = User.objects.get(pk=current_user.id)
        title = request.POST.get('title')
        myfile = None
        cat_obj = None
        category = request.POST.get('category')

        try:
            myfile = request.FILES['file']

        except:
            print("file not found")

        try:
            cat_obj = Category.objects.get(pk=category)
        except:
            print("cat_obj notvalid")

        
        

        tag = request.POST.get('tags')
        tag_list = tag.split(",")
        
        if len(title.split(" ")) > 2:
            if myfile:
                if len(tag_list) > 2:

                    if cat_obj is not None:
                        slug = slugify(title)
                        exslug = Ringtone.objects.filter(slug=slug).exists()
                        fs = FileSystemStorage()
                        filename = fs.save(f"urls/{title}.mp3", myfile)
                        uploaded_file_url = filename
                        all_image = imagelibrary.objects.filter(imagecategory_id=category).values('image')
                        liss = list(all_image)
                        spinreward = random.choice(liss)
                        finel = spinreward['image']
                        
                        
                        content = ''

                    
                        if exslug:
                            randomtext = generate()

                            randomslug = f"{slug}-{randomtext}"
                            # print(randomtext)
                            ringtone_obj = Ringtone.objects.create(
                                title=title, category=cat_obj, user=myuser,  slug=randomslug, file=uploaded_file_url, thumb=finel)
                            for item in tag_list:
                                ringtone_obj.tags.add(item)

                            myuser.points += 5

                            
                            ringtone_obj.save()
                            myuser.save()
                            
                        
                        else:

                            ringtone_obj = Ringtone.objects.create(
                                title=title, category=cat_obj, user=myuser,  slug=slug, file=uploaded_file_url,thumb=finel)

                            for item in tag_list:
                                ringtone_obj.tags.add(item)

                            myuser.points += 5
                            
                            ringtone_obj.save()
                            myuser.save()
                            
                        
                        
                        # ===============================
                        content += render_to_string('upload-ring.html', {'item': ringtone_obj},
                                                        request=request)
                        # ringtone_obj.save()

                        
                        return JsonResponse({"content" :content , "points":myuser.points, "added":5,})
                    return JsonResponse({"cat_error" :"Select category"})

                return JsonResponse({"tags_error" :"Enter atleast 2 tags"})        
            return JsonResponse({"file_error" :"file not valid"})
            
        return JsonResponse({"title_error" :"title lenth must be 2 words Above!"})
        
    else:
        getcat_obj = Category.objects.all()
        data = {
            "getcat_obj": getcat_obj,

        }
        return render(request, 'userload.html', data)


# User Signup


# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def signup(request):
    if request.method == "POST":
        # data = json.loads(request.body)

        dname = request.POST.get('dname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        is_valid = validate_email(email)
        is_valid = validate_email(email)
        print()
        if is_valid:
            if User.objects.filter(email=email).exists():
                return JsonResponse({"UserExists": "Email Already Exists try logging in"})
            else:
                if len(password) > 8:
                    user_obj = User.objects.create_user(
                        displayName=dname, email=email, password=password)
                    user_obj.save()
                    user = authenticate(email=email, password=password)
                    auth_login(request, user)
                    return JsonResponse({'success': 'Account created!'})

                return JsonResponse({"password_error": "Password Must be in 8 Above"})

        else:
            return JsonResponse({'email_error': 'Enter valid email address.'})
    else:
        if request.user.is_authenticated:
            return redirect('profile')
        return render(request, "signup.html")


def userlogin(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('profile')
        return render(request, 'login.html')

    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            return JsonResponse({'success': 'Login Success!'})
        else:
            return JsonResponse({"user_error": "Invalid Email & Password Enter Correct!"})


def userlogot(request):
    userlogout(request)
    return redirect('home')


@login_required(login_url='/login')
def profile(request):

    post_obj  = Ringtone.objects.filter(likes=request.user.id)
    profile = User.objects.get(pk=request.user.id)
    postscount  = Ringtone.objects.filter(user__id=request.user.id).count()
    posts  = Ringtone.objects.filter(user__id=request.user.id) 
    print(postscount)
    useradd = Profile.objects.get(pk=request.user.id)


    userfollowing = Profile.objects.get(pk=request.user.id)
    userfoing = userfollowing.following.all()
    em = useradd.followers.all()


    followingcount = userfollowing.followers_of
    emcount = userfollowing.following_of



    

    data= {
        "post_obj":post_obj,
        "em":em,
        "userfoing":userfoing,
        "followingcount":followingcount,
        "emcount":emcount,
        "postscount":postscount,
        "posts":posts,
        "profile":profile         
    }
    return render(request, "profile.html",data)


def ringtones(request):

    pagesite = "home"
    
    get_latest_ringtone = Ringtone.objects.all().order_by('-played')[:8]
    category_obj = Category.objects.all()
    category_obj_search = Category.objects.all()
    q_obj = suggestedsearch.objects.all().order_by('-query_count')[:6]
    seven_day_before =  datetime.datetime.now() - datetime.timedelta(days=7)
    last_7_day_trending = Ringtone.objects.filter(publishDate__gte=seven_day_before).order_by('-played')[:5]
    home_data = Home.objects.get(pk=1)
    SINGLE_RINGTONE_LIMIT = 1

    page = int(request.GET.get('page', 1))
    p = paginator.Paginator(category_obj,
                            SINGLE_RINGTONE_LIMIT)
    try:
        post_page = p.page(page)
    except paginator.EmptyPage:
        post_page = paginator.Page([], page, p)

    if request.method == "POST":

        content = ''
        for item in post_page:
            print(item.slug) 
            content += render_to_string('home-cat-loadmore.html', {'category_ob': item},
                                        request=request)
        return JsonResponse({
            "content": content,
            "end_pagination": True if page >= p.num_pages else False,
        })

    else:
        pagnumber = request.GET.get('page')
        if pagnumber is None:
            pagnumber = 1
        pagnumber


    data = {
        "get_latest_ringtone": get_latest_ringtone,
        "all_ringtone":"all_ringtone",
        "category_obj":post_page,
        "category_obj_search":category_obj_search,
        "q_obj":q_obj,
        "last_7_day_trending":last_7_day_trending,
        "pagnumber":pagnumber,
        "page":pagesite,
        "home_data":home_data
        
    
    }
    return render(request, 'ringtones.html', data)



    
   

@csrf_exempt 
def ringtone_played(request):
    try:
        ringtone_id = request.POST.get('ringtoneid')
        get_single_ringtone = Ringtone.objects.get(pk=ringtone_id)
        # if request.user.is_authenticated:
        #     get_single_ringtone.played += 1
        #     get_single_ringtone.save()
        #     return JsonResponse({"sucess":get_single_ringtone.played})

            
        if ringtone_id and not request.session.get(
            f"ringtone_played_{ringtone_id}", None
        ):
            get_single_ringtone.played += 1
            get_single_ringtone.save()
            request.session[f"ringtone_played_{ringtone_id}"] = True
            return JsonResponse({"result": True, "sucess":get_single_ringtone.played})

        return JsonResponse({"result": False}) 
    except:
        print("Ringtone Id Not Found!")   
        return JsonResponse({"STATUS": 404 , "Error":"Ringtone Id Not Found!" })
        
    



@csrf_exempt 
def rigntone_incress_download(request):
    data = {}
    for key, _ in request.POST.items():
        data = json.loads(key)

    ringtone_id = data.get("ringtone_id", None)
    if ringtone_id and not request.session.get(
        f"ringtone_download_{ringtone_id}", None
    ):
        # save_obj = Ringtone.objects.get(pk=int(ringtone_id))
        save_obj = Ringtone.objects.get(pk=ringtone_id)

        save_obj.downloads += 1
        save_obj.save()

        request.session[f"ringtone_download_{ringtone_id}"] = True

        ringtone_download_count = Ringtone.objects.get(pk=int(ringtone_id)).downloadsformated
        print("result :True ")

        return JsonResponse({"result": True, "download": ringtone_download_count})
    print("result :False ")
    return JsonResponse({"result": False})    

@csrf_exempt 
def rigntone_share(request):
    data = {}
    for key, _ in request.POST.items():
        data = json.loads(key)

    ringtone_id = data.get("ringtone_id", None)
    if ringtone_id and not request.session.get(
        f"ringtone_share_{ringtone_id}", None
    ):
        Ringtone.objects.filter(pk=int(ringtone_id)).update(share=F("share") + 1
        )
        request.session[f"ringtone_share_{ringtone_id}"] = True

        ringtone_share_count = Ringtone.objects.get(
            pk=int(ringtone_id)
        ).share
        return JsonResponse({"result": True, "share": ringtone_share_count})
    return JsonResponse({"result": False})    
@csrf_exempt 
@login_required(login_url='/login')
def ringtonelike(request):
    postid=request.POST.get('ringtone_id')

    post = Ringtone.objects.get(pk=postid)
    
    

    if post.likes.filter(id=request.user.id).exists():
        removeuser =  post.likes.remove(request.user)
        print(removeuser) 
        number_of_likes=post.number_of_likes()
        totl = list(str(number_of_likes))[0]
        return JsonResponse({"result": False, "user": removeuser, "tl":totl})
    else:
        removeuser = post.likes.add(request.user)
        print(f"user added {removeuser}")
        number_of_likes=post.number_of_likes()
        totl = list(str(number_of_likes))[0]
        return JsonResponse({"result": True, "user": removeuser , "tl":totl})

@csrf_exempt 
def ringtonelikefull(request):
    postid=request.POST.get('ringtone_id')

    post = Ringtone.objects.get(pk=postid)
    
    

    if post.likes.filter(id=request.user.id).exists():
         
        return JsonResponse({"result": True})
    removeuser = post.likes.add(request.user)
    print(f"user added {removeuser}")
    number_of_likes=post.number_of_likes()
    totl = list(str(number_of_likes))[0]
    return JsonResponse({"result": True, "user": "removeuser","tl":totl })
        
        
        

def singleringtone(request, slug):

    pagesite = "ringtone"
    home_data = Home.objects.get(pk=1)
    category_obj = Category.objects.all()
    q_obj = suggestedsearch.objects.all().order_by('-query_count')[:6]
    get_single_ringtone = Ringtone.objects.get(slug=slug)
    cat_slug = get_single_ringtone.category.slug
    get_reted_category = Ringtone.objects.filter(category__slug=cat_slug).exclude(pk=get_single_ringtone.id)
    
    followed = []
    if request.user.is_authenticated:
         
        user =User.objects.filter(email=get_single_ringtone.user).values_list('id', flat=True)
        list(user)
        print(user[0])
        useradd = Profile.objects.get(pk=user[0])
        # em = useradd.followers.all()
    
        follow = False
        if useradd.followers.filter(pk=request.user.id).exists():

            print(useradd.followers.count())

            follow = True
        # data['number_of_likes'] = get_single_ringtone.number_of_likes()
        # data['post_is_liked'] = liked
        
        followed = follow
    else:
        pass
   


    # =======================


    SINGLE_RINGTONE_LIMIT = 3

    page = int(request.GET.get('page', 1))
    p = paginator.Paginator(get_reted_category,
                            SINGLE_RINGTONE_LIMIT)
    try:
        post_page = p.page(page)
    except paginator.EmptyPage:
        post_page = paginator.Page([], page, p)

    if request.method == "POST":
 
        content = ''
        for item in post_page:
            print(item.slug) 
            content += render_to_string('cat-loadmore.html', {'item': item},
                                        request=request)
        return JsonResponse({
            "content": content,
            "end_pagination": True if page >= p.num_pages else False,
        })

    else:
        pagnumber = request.GET.get('page')
        if pagnumber is None:
            pagnumber = 1
        pagnumber

         
        # context = {
        # "get_category": post_page,
        # "pagnumber":pagnumber
        # }
        
        liked = False
        if get_single_ringtone.likes.filter(pk=request.user.id).exists():

            print(get_single_ringtone.likes)

            liked = True
    
        number_of_likes = get_single_ringtone.number_of_likes(),
        like = liked
        
        data = {
            "get_single_ringtone": get_single_ringtone,
            "get_reted_category":post_page,
            "number_of_likes":get_single_ringtone.number_of_likes(),
            "like":like,
            "category_obj":category_obj,
            "q_obj":q_obj,
            "followed":followed,
            "pagnumber":pagnumber,
            "page":pagesite,
            "home_data":home_data

            }
        return render(request, 'single_ringtone.html', data)
  



def tags(request, tag_slug):

    get_tag_ringtone = Ringtone.objects.filter(tags__slug=tag_slug)

    data = {
        "get_tag_ringtone":get_tag_ringtone
    }
    return render(request, 'tags.html', data)

NEWS_COUNT_PER_PAGE = 5

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def category(request, slug):
    get_category = Ringtone.objects.filter(category__slug=slug)
    get_all_categories_played = Ringtone.objects.filter(category__slug=slug).values_list('played', flat=True)
    category_info = Category.objects.get(slug=slug)
     
    catslug = category_info.slug
    ringtones_played = sum(get_all_categories_played)


    page = int(request.GET.get('page', 1))
    p = paginator.Paginator(get_category,
                            NEWS_COUNT_PER_PAGE)
    try:
        post_page = p.page(page)
    except paginator.EmptyPage:
        post_page = paginator.Page([], page, p)

    if request.method == "POST":
 
        content = ''
        for item in post_page:
            print(item.slug) 
            content += render_to_string('cat-loadmore.html', {'item': item},
                                        request=request)
        return JsonResponse({
            "content": content,
            "end_pagination": True if page >= p.num_pages else False,
        })

    else:
        pagnumber = request.GET.get('page')
        if pagnumber is None:
            pagnumber = 1
        pagnumber

        print(pagnumber)
         
        context = {
        "get_category": post_page,
        "category_info":category_info,
        "ringtones_played":ringtones_played,
        "pagnumber":pagnumber
        }
        
      
        return render(request,
                      'category_ringtone.html',
                      context)
    
    # print(get_category.count())
    # print(type(get_category))
    

 
     
        
         
    # print(category_name.name)
    # data = {
    #     "get_category": get_category,
    #     "category_info":category_info,
    #     "ringtones_played":ringtones_played
    #      }
    # return render(request, 'category_ringtone.html', data)


@csrf_exempt
def search_ringtone(request):
    query = request.POST.get("query")
     
    if query:
        
        ringtone_objects = Ringtone.objects.filter(title__icontains=query)
        category_objects = Category.objects.filter(title__icontains=query)
        print(ringtone_objects)
        results = []
        catobj = []
        for ringtone in ringtone_objects:
            
            object = {}
            object["category_name"] = ringtone.category.name
         
            object["ringtone_name"] = ringtone.title
            object["ringtone_url"] = ringtone.slug
            object["category_url"] = ringtone.category.slug
            object["ringtone_img"] = ringtone.thumb.url
            object["ringtone_file"] = ringtone.file.url
           
            object["ringtone_plays"] = ringtone.played
            object["ringtone_id"] = ringtone.id
            object["ringtone_downloads"] = ringtone.downloadsformated

            results.append(object)
        for cat in category_objects:
            objectt = {}

            objectt["category_name"] = cat.name
            catobj.append(objectt)    



             
        return JsonResponse({"query": query, "ringtones": results , "cates":catobj})
    return JsonResponse({"query_error": "Not found"})
    
@csrf_exempt    
def suggsearch(request):
    search_query = request.POST.get("search_query")
    suggq = suggestedsearch.objects.filter(query=search_query).exists()
    
    if suggq:
        q_check = suggestedsearch.objects.get(query=search_query)
        q_check.query_count += 1
        q_check.save()
         
        return JsonResponse({"result":search_query})  
    suggsearch = suggestedsearch.objects.create(query=search_query,query_count=1)
    return JsonResponse({"result":f"{search_query} saved"})


def userprofile(request, pk):

    # try:
        profile = User.objects.get(pk=pk)
        postscount  = Ringtone.objects.filter(user__id=pk).count()
        posts  = Ringtone.objects.filter(user__id=pk) 
        useradd = Profile.objects.get(pk=pk)

        
        profileuserfollowing = Profile.objects.get(pk=pk)

        
        
        userfoing = profileuserfollowing.following.all()
        em = profileuserfollowing.followers.all()
    
    
        followingcount = profileuserfollowing.followers_of
        emcount = profileuserfollowing.following_of
    

        postscount  = Ringtone.objects.filter(user__id=pk).count()
        posts  = Ringtone.objects.filter(user__id=pk) 
        follow = False
        login = False
        if useradd.followers.filter(pk=request.user.id).exists():

            follow = True
            login = True
        
        followed = follow
        logged = login

         
        

        data  = {
            "followingcount":followingcount,
            "emcount":emcount,
            "userfoing":userfoing,
            "em":em,
            "postscount":postscount,
            "posts":posts,
            "profile":profile,
            "followed":followed,
            "logged":logged
        }

        return render(request , 'userprofile.html', data)
    # except:
    #     return JsonResponse({"error":"User Not Found"})
    # return JsonResponse({"profile":profile.name , "postscount":postscount})

@csrf_exempt    
def addfollow(request):
    pk = request.POST.get("userID")
    if request.user.is_authenticated:
        print(f"USER ID : {pk}")
        profile =  Profile.objects.get(pk=pk)
        profile2 = Profile.objects.get(pk=request.user.id)
        # ============
        # user =User.objects.filter(email=get_single_ringtone.user).values_list('id', flat=True)
        # list(user)
        # print(user[0])
        # useradd = Profile.objects.get(pk=request.user.id)

        # print(profile.user)
        # ======
        
        if profile.followers.filter(pk=request.user.id).exists():

            useradd = profile.followers.remove(request.user)
            tst = profile2.following.remove(profile.user)

            print(f"Unfollowed : {profile.user.displayName}")
           
            followingcount = profile.followers.count()
            profile2.save()
           
            return JsonResponse({
                "profile":"User Removed",
                "followingcount":followingcount,
                "Unfollowed":profile.user.displayName,
                "result":False,
            })
        else:
            useradd = profile.followers.add(request.user)
            profile2.following.add(profile.user)

            followingcount = profile.followers.count()
            # print(f"followed : {profile.user.displayName}")
            return JsonResponse({
                "profile":"User Added",
                "followed":profile.user.displayName,
                "followingcount":followingcount,
                "result":True,
            })
            
    else:
        return JsonResponse({
                "add_error":False,
                "result":False,
            })


@login_required(login_url='/login')
def profile_update(request):
    current_user = request.user
    if request.method=="POST":
 
        myuser = User.objects.get(pk=current_user.id)
        displayname = request.POST.get('name')
        number = request.POST.get('number')
        bio = request.POST.get('bio')
        insta = request.POST.get('insta')
        youtube = request.POST.get('youtube')
        instaurl = "instagram"
        youtubeurl = "youtube"

 

        error_msg = None

        print(len(displayname))
        if (not displayname):
            error_msg = "Name is Required!"
            
        elif len(displayname) < 4:
            error_msg = "Name is long than 5"
        elif (not number):
            error_msg = "Number is Required!"
        elif len(number) < 10:
            error_msg = "Invalid Number!"
        elif len(number) > 10:
            error_msg = "Invalid Number!"
            

            

        print(error_msg)
        if (not error_msg):
            newdisplayname = myuser.displayName=displayname
            newnumber = myuser.paytm_num=number
            newbio = myuser.bio=bio
            newinsta = myuser.insta=insta
            newyoutube = myuser.youtube=youtube
            myuser.save()
            return JsonResponse({"staus":"ok"})

    return JsonResponse({"error_msg":error_msg})



@login_required(login_url='/login')
def profile_pic_update(request):
    if request.method =="POST":
        current_user = request.user
        myuser = User.objects.get(pk=current_user.id)
        myfile = request.FILES['file']
       
        fs = FileSystemStorage()
        
        filename = fs.save(f'profile/{myfile.name}', myfile)

        file_url = myuser.profile_image = filename 

        myuser.save()
        return JsonResponse({"file_status":file_url})
       
       
            
        
 
def useredeem(request):
    profile = User.objects.get(pk=request.user.id)
    usernxt  = request.POST.get('usernxt')
    if request.method == "POST":

        if int(usernxt) >= 1000:

            point = profile.points 
            redeem = "redeem"
            cash = "cash"

            value  = int(usernxt) * 5/100

            print(value)

            payment = None

            if point > 1000:
                payment = redeem,
            payment = cash


            pay= Payment.objects.create(user=profile,mobile_number=profile.paytm_num,payment_type=payment , inr=value)

            return JsonResponse({"":""})
        return JsonResponse({"limit_error":"You Need More NXT to Redeem"})

   
     
    plan = Plans.objects.get(pk=5)
    pen =   profile.points /plan.point*100
    point_left = plan.point - profile.points 
    print(point_left)
    
    print(plan)
    data = {
        "profile":profile,
        "plan":plan,
        "pen":pen,
        "point_left":point_left
    }


    return render(request , 'redeme.html', data)