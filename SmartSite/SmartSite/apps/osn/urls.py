from django.urls import path
from . import views
from django.http import Http404,HttpResponseRedirect
app_name="osn"
urlpatterns=[
    path('',views.index,name="index"),
    path('<int:Priloshenie_id>/',views.detail,name="detail")
]