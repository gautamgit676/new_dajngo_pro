from django.urls import path
from .views import SchoolDataAPI, Userform

urlpatterns = [
    path('demoapi/',SchoolDataAPI.as_view(), name='demoapi'),
    path('userform/', Userform.as_view(), name='userform'),
 
]