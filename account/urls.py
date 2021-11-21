from django.urls import path
from .views import user_list, user_profile, login_view, logout_view

app_name = 'account'

urlpatterns = [
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>', user_profile, name='user_profile'),
]