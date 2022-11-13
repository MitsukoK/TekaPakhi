from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework.permissions import IsAuthenticated
from userapp.models import NewUser
from userapp.serializer import NewUserSerializer

# Create your views here.


class LogoutView(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=HTTP_200_OK)


class UserView(APIView):
    def get(self, req):
        return Response("user page", status=HTTP_200_OK)


# get user details
class UserDetailView(APIView):
    def get(self, req):
        # check if user is authenticated
        if req.user.is_authenticated:

            # get the user details
            _user = NewUser.objects.filter(username=req.user.username)
            # _user = NewUser.objects.get(id=req.user.id)
            print("this is user", _user.values()[0])
            serializer = NewUserSerializer(_user, many=True)
            # user_name = _user.values()[0]["username"]
            # first_name = _user.values()[0]["first_name"]
            # last_name = _user.values()[0]["last_name"]
            # email = _user.values()[0]["email"]
            # is_staff = _user.values()[0]["is_staff"]
            # is_active = _user.values()[0]["is_active"]
            # date_joined = _user.values()[0]["date_joined"]
            # phone_number = _user.values()[0]["phone_number"]
            # client_identity_id = _user.values()[0]["client_identity_id"]
            # current_balance = _user.values()[0]["current_balance"]
            # user_pin = _user.values()[0]["user_pin"]
            # mobile_banking = _user.values()[0]["mobile_banking"]
            # mobile_recharge = _user.values()[0]["mobile_recharge"]
            # bank = _user.values()[0]["bank"]
            return Response(serializer.data, status=HTTP_200_OK)
            # return Response("user details", status=HTTP_200_OK)

        return Response("user not authenticated", status=HTTP_200_OK)
