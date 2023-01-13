from django.contrib import admin

from .models import Flat, Complaint, Owner


# admin.site.register(Flat)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'owners_phonenumber', 'owner_pure_phone', 'price', 'new_building',
                    'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'town', 'address',)
    raw_id_fields = ('liked_by',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
