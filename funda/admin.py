from django.contrib import admin
from django.utils.html import format_html
from reversion.admin import VersionAdmin
from reversion_compare.admin import CompareVersionAdmin

from django.contrib.admin.utils import flatten_fieldsets

from .models import Woning


@admin.register(Woning)
class WoningAdmin(CompareVersionAdmin):
    list_filter = ('verkoop_status', 'eigendoms_situatie')
    list_display = (
        'adres', 'get_url_display', 'koopprijs', 'verkoop_status', 'cv',
        'oppervlakte', 'perceeloppervlakte', 'postcode')
    list_editable = ('notes', 'interessant')

    def get_fieldsets(self, request, obj=None):
        return [
            (None, {
                'fields': ('adres', 'koopprijs', 'verkoop_status', 'cv',
                           'oppervlakte', 'perceeloppervlakte', 'postcode')
            }),
            ('Overige', {'fields': self.get_fields(request, obj)})
        ]

    def get_readonly_fields(self, request, obj=None):
        return list(set(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]
        ))

    def get_url_display(self, obj):
        return format_html('<a href="{}">Bekijk op Funda</a>'.format(obj.url))

