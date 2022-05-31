from django.urls import path
from user.views import *

urlpatterns = [
    path('adduser',addUser.as_view({'post':'create'}),name="adduser"),
    path('check',check.as_view({'get':'list'}),name="check"),
]