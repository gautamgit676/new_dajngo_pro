from django.urls import path
from .views import SchoolDataAPI, Userform,userdata,studentform,Userlogin

urlpatterns = [
    path('demoapi/',SchoolDataAPI.as_view(), name='demoapi'),
    path('userform/', Userform.as_view(), name='userform'),
    path('userdata/', userdata.as_view(), name='userdata'),
    path('stu/', studentform.as_view(), name='stu'),
    path('userlogin/', Userlogin.as_view(), name='userlogin'),
 
]