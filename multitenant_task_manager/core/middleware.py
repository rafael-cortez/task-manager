# middleware.py
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class AdminRestrictMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')):
            if request.get_host() != settings.PUBLIC_SCHEMA_DOMAIN:
                return redirect(settings.ADMIN_RESTRICT_REDIRECT_URL)
        response = self.get_response(request)
        return response
