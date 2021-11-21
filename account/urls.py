from django.urls import path
from .views import user_list, user_profile

app_name = 'account'

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>', user_profile, name='user_profile'),
]