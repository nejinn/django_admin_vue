from rest_framework_jwt.views import ObtainJSONWebToken
from datetime import datetime
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from nui.utils.response_msg.server_msg import LOGIN_USER_NOT_EXIST, LOGIN_USER_IS_ACTIVE, LOGIN_USER_IS_STAFF, \
    LOGIN_USER_ACCOUNT_ERROR, REGISTER_MODEL_ERROR
from nui.utils.response_data.response import ResponseDate
from rest_framework.views import APIView
import nui
from django.utils.translation import gettext as _, ngettext
from django.core import serializers

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


class ModelList(APIView):

    def get(self, request, app_label, model_name):
        x = nui.site._registry
        register_obj = None
        model_obj = None
        for m, l in x.items():
            if m._meta.app_label == app_label and m._meta.model_name == model_name:
                register_obj = l
                model_obj = m
                break

        if register_obj is None or model_obj is None:
            return ResponseDate.json_data(service_type=REGISTER_MODEL_ERROR)

        opts = register_obj.model._meta

        cl, res = register_obj.nui_get_changelist_instance(request)
        selection_note_all = ngettext(
            '%(total_count)s selected',
            'All %(total_count)s selected',
            cl.result_count
        )

        context = {
            **register_obj.admin_site.each_context(request),
            'module_name': str(opts.verbose_name_plural),
            'selection_note': _('0 of %(cnt)s selected') % {'cnt': len(cl.result_list)},
            'selection_note_all': selection_note_all % {'total_count': cl.result_count},
            'title': cl.title,
            'is_popup': cl.is_popup,
            'to_field': cl.to_field,
            'cl': res,
            'has_add_permission': register_obj.has_add_permission(request),
            # 'opts': cl.opts,
            'actions_on_top': register_obj.actions_on_top,
            'actions_on_bottom': register_obj.actions_on_bottom,
            'actions_selection_counter': register_obj.actions_selection_counter,
            'preserved_filters': register_obj.get_preserved_filters(request),
        }

        return ResponseDate.json_data(context)
