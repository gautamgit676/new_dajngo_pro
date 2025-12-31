
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.

# demo api 
class SchoolDataAPI(APIView):
    def get(self, request):
        return Response({"message": "Hello, this is a demo API response!"})



class Userform(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username:
            return Response({"error": "Username is required"}, status=400)

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        return Response({"message": "User created successfully!"}, status=201)

