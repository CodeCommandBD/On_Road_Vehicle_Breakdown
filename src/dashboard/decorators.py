from django.http import HttpResponseRedirect
from django.urls import reverse
from functools import wraps


def staff_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('staff_login_view'))

    return _wrapped_view

