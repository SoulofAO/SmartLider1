from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment,Priloshenie,ButtonFind
from django.urls import  reverse
# Create your views here.
from django.http import Http404,HttpResponseRedirect
import time
from django.contrib.auth import login, authenticate, logout
def index(request,Priloshenie_id=""):
    print(1)
    try:
        a=Priloshenie.objects.get(id=Priloshenie_id)
        Name = request.POST["name"]
    except:
        Name=""
    if Name == "":
        last = Priloshenie.objects.order_by("Text")
        return render(request, "apps/list.html", {"last": last})
    else:
        last = Priloshenie.objects.get(name=Name)
        return render(request, "apps/list.html", {"last": last})


def detail(request, Priloshenie_id):
    try:
        a=Priloshenie.objects.get(id=Priloshenie_id)
    except:
        raise Http404("Что то пошло не так")
    last_comment=a.comment_set.order_by('id')
    return render(request,"apps/detail.html",{"Priloshenie":a,"last_comment":last_comment})


def comment(request,Priloshenie_id,name,text):
    try:
        a=Priloshenie.objects.get(id=Priloshenie_id)
    except:
        raise Http404("Что то пошло не так")


    print(name,text,00000000000000000000000000000000)
    Comment.objects.create(
    priloshenie=a, Text=text,
    Name=name)
    return HttpResponseRedirect(reverse('osn:detail',args=(a.id,)))



def test(request):
    if request.method == "POST":
       a=request.POST.get("find")
       print(a)
       last=Priloshenie.objects.filter(Name=a)
       print (last)
       return render(request, "apps/list.html", {"last": last})
    else:
        return None


def login_user (request):
    if 'username' and 'password' in request.GET:
        user = authenticate (username = request.GET['username'],
                        password = request.GET['password'])
        if user.is_active:
            login (request, user)
            return render('bc/account_page.html', locals ())
        else:
            pass
    else:
        return render('bc/login_page.html')


def new_user_registration(request):
    errors = []
    if 'user' and 'pass' and 'email' in request.GET:
        if User.objects.filter(username=request.GET['user']):
            errors.append('that username zanyato')
            return render('bc/registration_page.html', locals())

        new_user = User.objects.create_user(request.GET['user'],
                                            request.GET['pass'],
                                            request.GET['email'])

        return HttpResponseRedirect('/bc/registration_complete/', locals())
    else:
        return render('bc/registration_page.html/', locals())
