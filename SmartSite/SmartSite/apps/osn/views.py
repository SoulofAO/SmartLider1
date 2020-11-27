from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment,Priloshenie,ButtonFind
# Create your views here.
from django.http import Http404,HttpResponseRedirect
def index(request):
    last=Priloshenie.objects.order_by("Text")[:5]
    return render(request,"apps/list.html",{"last":last})
def detail(request, Priloshenie_id):
    try:
        a=Priloshenie.objects.get(id=Priloshenie_id)
    except:
        raise Http404("Что то пошло не так")
    return render(request,"Priloshenie/detail.html",{"Priloshenie":a})