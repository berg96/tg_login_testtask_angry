from django.urls import path
from .views import home, login_by_telegram, check_auth_status

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_by_telegram, name='login_by_telegram'),
    path('auth-status/', check_auth_status, name='auth_status'),
]
