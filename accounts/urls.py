from django.urls import path
from . import views
# from .views import login_view
# from .views import register_view
from .views import register

urlpatterns = [
    path("", views.loginForm),
    # path("loginview/", login_view, name="loginview"),
    # path("registerview/", register_view, name="loginview"),
    path('register/', register, name='register'),

]




