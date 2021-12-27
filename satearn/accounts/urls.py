from django import views
from django.urls import path

from .views import SignUpView, profile

app_name = 'accounts'
urlpatterns = [
    # ex: /accounts/signup/
    path('signup/', SignUpView.as_view(), name='signup'),
    # ex: /accounts/32/
    path('<int:user_id>/', profile, name='profile')
]