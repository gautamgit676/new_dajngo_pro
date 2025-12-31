
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
import logging
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAdminUser

# Create your views here.

# demo api 
class SchoolDataAPI(APIView):
    def get(self, request):
        return Response({"message": "Hello, this is a demo API response!"})




# class UserCreateAPIView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = userser(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {"message": "User created successfully"},
#                 status=201
#             )
#         return Response(serializer.errors, status=400)

# 
class Userlogin(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"error": "Invalid username or password"},
                status=401
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "User logged in successfully",
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }, status=200)

# 
class Userform(APIView):
    def post(self, request):
        userserlizer = userser(data=request.data)
        if userserlizer.is_valid():
            userserlizer.save()
            return Response({"message": "User created successfully!"}, status=201)
        return Response(userserlizer.errors, status=400)



class userdata(APIView):
    def get(self, request):
        users = User.objects.all()
        userserlizer = userser(users, many=True)
        return Response(userserlizer.data)
    
from .models import STUDENT

class studentform(APIView):
    def get (self, request):
        students = STUDENT.objects.all()
        studserlizer = studentser(students, many=True)
        return Response(studserlizer.data)
    
    def post(self, request):
        studserlizer = studentser(data=request.data)
        if studserlizer.is_valid():
            studserlizer.save()
            return Response({"message": "Student created successfully!"}, status=201)
        return Response(studserlizer.errors, status=400)
    
