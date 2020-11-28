from django.core.exceptions import PermissionDenied
from .models import UserProfile,User


def user_is_role_adm(function):
    def wrap(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['user_id'])
        if user.profile.role == 'admin' or user.profile.role == 'doctor':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap