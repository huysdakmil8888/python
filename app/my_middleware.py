from django.urls import reverse
from django.shortcuts import redirect
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import exceptions

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # jwt_auth = JWTAuthentication()
        # try:
        #     user, validated_token = jwt_auth.authenticate(request)
        #     request.user = user
        # except exceptions.AuthenticationFailed:
        #     pass
        return self.get_response(request)