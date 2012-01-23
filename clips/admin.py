from django.contrib import admin
from clips.models import Clip

class ClipAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Clip, ClipAdmin)