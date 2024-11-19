from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URLs that do not require login
        exempt_urls = [reverse('login'), reverse('signup')]

        # Redirect to login if the user is not logged in and tries to access a protected URL
        if not request.session.get('user_id') and request.path not in exempt_urls:
            return redirect('login')
        
        response = self.get_response(request)
        return response
