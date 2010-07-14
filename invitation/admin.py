from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from registration.backends.invitation.models import InvitationCode


class InvitationCodeAdmin(admin.ModelAdmin):
    """Admin for invitation code"""
    fields = ('code', 'is_used', 'user', 'used_date', )
    readonly_fields = ('code', 'is_used', 'user', 'used_date', )
    list_display = ('code', 'is_used', 'user', 'used_date', )
    list_filter = ('is_used', 'used_date', )

admin.site.register(InvitationCode, InvitationCodeAdmin)
