from rest_framework_jwt.views import ObtainJSONWebToken
from datetime import datetime
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from utils.response_msg.server_msg import LOGIN_USER_NOT_EXIST, LOGIN_USER_IS_ACTIVE, LOGIN_USER_IS_STAFF, \
    LOGIN_USER_ACCOUNT_ERROR
from utils.response_data.response import ResponseDate
from rest_framework.views import APIView
import nui
from django.utils.translation import gettext as _

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


# Create your views here.

# admin 登录
class UserLoginAPIView(ObtainJSONWebToken):
    serializer_class = JSONWebTokenSerializer

    @staticmethod
    def get(request):
        context = {
            **nui.site.each_context(request),
            'title': _('Log in'),
            'app_path': request.get_full_path(),
            'username': request.user.get_username(),
        }

        return ResponseDate.json_data(context)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')

            user_id = user.id
            admin_user = User.objects.filter(id=user_id).first()

            if not admin_user:
                return ResponseDate.json_data(service_type=LOGIN_USER_NOT_EXIST)

            if not admin_user.is_active:
                return ResponseDate.json_data(service_type=LOGIN_USER_IS_ACTIVE)

            if not admin_user.is_staff:
                return ResponseDate.json_data(service_type=LOGIN_USER_IS_STAFF)
            response_data = jwt_response_payload_handler(token, user, request)
            response = ResponseDate.json_data(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            return response

        return ResponseDate.json_data(service_type=LOGIN_USER_ACCOUNT_ERROR)


# sidebar
class UserSidebarAPIView(APIView):

    def get(self, request, extra_context=None):
        side_props = nui.site.get_side_props(request)

        context = {
            **nui.site.each_context(request),
            'title': nui.site.index_title,
            'app_list': side_props,
            'user_info': request.user.username,
            **(extra_context or {}),
        }

        return ResponseDate.json_data(context)
