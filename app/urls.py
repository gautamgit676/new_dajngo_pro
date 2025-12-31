from django.urls import path
from .views import SchoolDataAPI, Userform,userdata,studentform

urlpatterns = [
    path('demoapi/',SchoolDataAPI.as_view(), name='demoapi'),
    path('userform/', Userform.as_view(), name='userform'),
    path('userdata/', userdata.as_view(), name='userdata'),
    path('studentform/', studentform.as_view(), name='studentform'),
 
]