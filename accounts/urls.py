from django.urls import path
from . import views
# from .views import login_view
# from .views import register_view
from .views import register

urlpatterns = [
    path("login/", views.login_view, name='login'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('logout/', views.logout_view, name='logout'),

]




