from django.contrib import admin

from accounts.models import Names, Spares

# Register your models here.
admin.site.register(Spares)
admin.site.register(Names)