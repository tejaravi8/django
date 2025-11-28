from django.urls import path
from .views import addemp, created

urlpatterns = [
    path("",addemp),
    path("add/",created,name="teja"),
]


# from . import views

# urlpatterns = [
#     path("",views.addemp),
# ]