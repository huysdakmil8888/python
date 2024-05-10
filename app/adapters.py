# adapters.py

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        sociallogin.account.user = user
        sociallogin.account.save()
        sociallogin.account.refresh_avatar_url(request)
        print('user1 ',user)

        return user

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        sociallogin.account.user = user
        sociallogin.account.save()
        sociallogin.account.refresh_avatar_url(request)
        print('user2 ',user)
        return user