from django.urls import path
from . import views, api_views
# from .views import login_view
# from .views import register_view
from .views import register

urlpatterns = [
    path("login/", views.login_view, name='login'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path("api/login/", api_views.LoginAPIView.as_view(), name='api-login'),
    path("api/register/", api_views.RegisterAPIView.as_view(), name='api-register'),
    path("api/profile/", api_views.ProfileAPIView.as_view(), name='api-profile'),

]




