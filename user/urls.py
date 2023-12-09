from django.urls import path
from .views import UserProfileView, user_registration_view, user_login_view, AccountSettingsView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('register/', user_registration_view, name='user-registration'),
    path('login/', user_login_view, name='user-login'),
    path('account/settings/', AccountSettingsView.as_view(), name='account-settings'),
]