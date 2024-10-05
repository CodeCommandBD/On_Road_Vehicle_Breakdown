# csrf_cookie_middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.middleware.csrf import get_token


class EnsureCsrfCookieMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        """
        Ensures that a CSRF token is set in the user's cookies.
        The token is set only if it's not already present.
        """
        # Get the CSRF token. This ensures a token is created if not already.
        get_token(request)

        return response
