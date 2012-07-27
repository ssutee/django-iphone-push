from django.contrib import admin
from iphonepush.models import iPhone

class iPhoneAdmin(admin.ModelAdmin):
    list_display = ('udid', 'notes', 'test_phone',)

admin.site.register(iPhone, iPhoneAdmin)