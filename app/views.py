
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import userser
# Create your views here.

# demo api 
class SchoolDataAPI(APIView):
    def get(self, request):
        return Response({"message": "Hello, this is a demo API response!"})



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

