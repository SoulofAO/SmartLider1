from django.shortcuts import render
from django.http import HttpResponse

from django.forms import ModelForm,TextInput,Textarea
# Create your views here.
def create(request):
    if request=="POST":
        a = request.POST.get("ber")
        print(a)
        return render(request, 'main/find.html')




def home(request):
    return render(request,'main/index.html')

