# my_middleware.py
from django.urls import reverse
from django.shortcuts import redirect


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        login_url = reverse('login')
        signup_url = reverse('signup')
        home_url = reverse('home')

        if request.path != login_url and not request.user.is_authenticated:
            return redirect(login_url)
        elif request.path == login_url and request.user.is_authenticated:
            return redirect(home_url)
        response = self.get_response(request)
        return response