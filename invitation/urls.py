"""
URLconf for registration and activation, using django-registration's
invitation backend.

"""


from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from registration.views import activate, register


urlpatterns = patterns('',
    url(r'^activate/complete/$', direct_to_template,
        {'template': 'registration/activation_complete.html', },
        name='registration_activation_complete'),

    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the view
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.
    url(r'^activate/(?P<activation_key>\w+)/$',
        activate,
        {'backend': 'registration.backends.invitation.InvitationBackend' },
        name='registration_activate'),
    url(r'^register/$',
        register,
        {'backend': 'registration.backends.invitation.InvitationBackend'},
        name='registration_register'),

    url(r'^register/complete/$',
        direct_to_template,
        {'template': 'registration/registration_complete.html' },
        name='registration_complete'),
    url(r'^register/complete/ajax/$',
        direct_to_template,
        {'template': 'registration/registration_complete_ajax.html' },
        name='registration_complete_ajax'),

    url(r'^register/closed/$',
        direct_to_template,
        {'template': 'registration/registration_closed.html' },
        name='registration_disallowed'),
    (r'', include('registration.auth_urls')),
)
