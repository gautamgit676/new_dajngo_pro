from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
# password incript

class userser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password','email']
        extra_kwargs = {'password': {'write_only': True}}
        
        # fields = "__all__"
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class studentser(serializers.ModelSerializer):  
    class Meta:
        from .models import STUDENT
        model = STUDENT
        fields = '__all__'

