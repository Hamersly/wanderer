from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class TlModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('title','content')


class RsModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('map', 'content')


class OutfitModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


admin.site.register(TL, TlModelAdmin)
admin.site.register(Rs, RsModelAdmin)
admin.site.register(Rubrics)
admin.site.register(Outfit, OutfitModelAdmin)
