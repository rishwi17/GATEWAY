from django.contrib import admin
from .models import Complaint

# Register your models here.
class ComplaintInline(admin.TabularInline):
    model = Complaint


class ComplaintAdmin(admin.ModelAdmin):
    readonly_fields = ("flat",)


admin.site.register(Complaint, ComplaintAdmin)
