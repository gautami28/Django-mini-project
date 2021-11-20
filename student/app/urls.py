from django.urls import path
from . import  views

urlpatterns = [
    path('',views.register.as_view(),name="home"),
    path('succ/',views.success,name="success")

]