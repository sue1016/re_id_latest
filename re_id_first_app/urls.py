from django.urls import path
from . import views
# from views import img_proc


urlpatterns = [
    path('', views.img_proc),
    path('test/', views.home)
]
