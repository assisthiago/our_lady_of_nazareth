from django.contrib import admin

from .models import Mystery


@admin.register(Mystery)
class MysteryAdmin(admin.ModelAdmin):

    list_display = ['name', 'sequence', 'category']

    ordering = ('category', 'sequence',)

    class Meta():
        order_by = ('category', 'sequence',)
