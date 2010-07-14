from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class InvitationCode(models.Model):
    """Invitation code model"""
    code = models.CharField(blank=True, max_length=5, unique=True,
        verbose_name=_(u"Invitation code"))
    is_used = models.BooleanField(default=False,
        verbose_name=_(u"Is code used?"))
    user = models.ForeignKey(User, blank=True, null=True)
    used_date = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        verbose_name=_(u"Used on"))
