from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class LogoutView(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=HTTP_200_OK)


class UserView(APIView):
    def get(self, req):
        return Response("user page", status=HTTP_200_OK)
