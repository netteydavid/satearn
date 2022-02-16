from django.contrib import admin

from .models import Application, Bounty, Invoice

admin.site.register(Bounty)
admin.site.register(Invoice)
admin.site.register(Application)