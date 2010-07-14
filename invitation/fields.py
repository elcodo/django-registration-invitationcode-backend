from django import forms
from django.utils.translation import ugettext_lazy as _
from registration.backends.invitation.models import InvitationCode


class InvitationCodeField(forms.CharField):
    """Invitation code field"""

    def validate(self, value):
        """Validate against invitation code table"""
        super(InvitationCodeField, self).validate(value)

        try:
            invitation_code = InvitationCode.objects.get(is_used=False,
                code=value)
        except InvitationCode.DoesNotExist:
            raise forms.ValidationError(_("Invalid invitation code."))
