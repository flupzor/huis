from django.contrib import admin
from django.contrib.admin.utils import flatten_fieldsets
from django.db import models
from django.forms import Textarea
from django.utils.html import format_html
from reversion.admin import VersionAdmin
from reversion_compare.admin import CompareVersionAdmin

from .models import Woning


@admin.register(Woning)
class WoningAdmin(CompareVersionAdmin):
    list_filter = ('verkoop_status', 'eigendoms_situatie')
    list_display = (
        'adres', 'get_url_display', 'koopprijs', 'get_beschikbaar', 'notes',
        'interessant', 'cv', 'oppervlakte', 'perceeloppervlakte', )
    list_editable = ('notes', 'interessant')

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

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

    def get_beschikbaar(self, obj):
        return obj.verkoop_status == 'StatusBeschikbaar'
    get_beschikbaar.boolean = True
    get_beschikbaar.short_description = 'beschikbaar'

    def get_url_display(self, obj):
        return format_html('<a href="{}">Bekijk op Funda</a>'.format(obj.url))
    get_url_display.short_description = 'bekijk op funda'

