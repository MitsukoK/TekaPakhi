from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.response import Response


class LogOutView(APIView):
    """log out view for user"""

    def post(self, req):
        req.user.auth_token.delete()
        return Response(status=HTTP_200_OK)


class UserView(APIView):
    def get(self, req):
        return Response("user page", status=HTTP_200_OK)
