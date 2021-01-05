from django.urls import path
from nui.views import *

urlpatterns = [
    path('login/', UserLoginAPIView.as_view()),
    path('sidebar/', UserSidebarAPIView.as_view()),

]
