from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.simple_upload, name="upload"),
    path('api', views.get_api, name="get"),
    path('api/post', views.send_api, name="send"),
    path('api/recive', views.recieve, name="recive")
]