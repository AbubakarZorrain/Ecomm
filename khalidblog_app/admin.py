import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import *
# Register your models here.
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"
@admin.register(Post)
class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("title",  "url", "content","image","pub_date","last_edited","author")
    list_filter = ("title", "url", "content","image","pub_date","last_edited","author")
    actions = ["export_as_csv"]