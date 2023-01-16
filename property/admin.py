from django.contrib import admin

from .models import Flat, Complaint, Owner


# admin.site.register(Flat)


class OwnersInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'town', 'address',)
    raw_id_fields = ('liked_by',)
    inlines = [
        OwnersInline
    ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ('name',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
