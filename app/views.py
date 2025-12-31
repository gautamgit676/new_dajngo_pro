
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

# demo api 
class SchoolDataAPI(APIView):
    def get(self, request):
        return Response({"message": "Hello, this is a demo API response!"})







