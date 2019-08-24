from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class TLAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('title', 'content')


admin.site.register(TL, SomeModelAdmin)
