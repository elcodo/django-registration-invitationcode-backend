from django import forms
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.invitation.fields import InvitationCodeField

attrs_dict = {'class': 'required'}


class RegistrationFormInvitationCode(RegistrationFormUniqueEmail):
    """Form extending RegistrationFormUniqueEmail.
    Adds two fields - invitation_code and tos for invitation code and TOS
    accept to proceed.

    """
    invitation_code = InvitationCodeField(required=True, max_length=5,
        label=_(u"Invitation code"))
    tos = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict),
                            label=_(u'I have read and agree to the Terms of ' \
                                    u' Service'),
                            error_messages={'required': _("You must agree " \
                                    u"to the terms to register")})
