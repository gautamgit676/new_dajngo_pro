from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets


class userser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



