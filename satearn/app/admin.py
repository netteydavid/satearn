from django.contrib import admin

from .models import Bounty, Invoice

admin.site.register(Bounty)
admin.site.register(Invoice)
