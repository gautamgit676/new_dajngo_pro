from django.urls import path
from .views import SchoolDataAPI

urlpatterns = [
    path('demoapi/',SchoolDataAPI.as_view(), name='demoapi')
 
]