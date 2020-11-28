from django.urls import path
from . import views

app_name="osn"
urlpatterns=[
    path('test', views.test, name="test"),
    path('', views.index, name="index"),
    path('<int:Priloshenie_id>/', views.detail, name="detail"),
    path('<int:Priloshenie_id>/comment', views.comment(), name="comment"),
    path("register",views.login_user, name="login_user,")
]
