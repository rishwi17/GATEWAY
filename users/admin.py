from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ResidentCreationForm, ResidentUpdateForm
from .models import Resident, Vehicle, Visitor

from complaints.admin import ComplaintInline


class VehicleInline(admin.TabularInline):
    model = Vehicle


class VisitorInline(admin.TabularInline):
    model = Visitor


class VisitorAdmin(admin.ModelAdmin):
    list_display = ['name', 'purpose', 'number']
    readonly_fields = ['entryTime', 'flat']


class ResidentAdmin(UserAdmin):
    add_form = ResidentCreationForm
    form = ResidentUpdateForm
    model = Resident
    list_display = ["username", "flatNo", "is_verified"]
    search_fields = ['username', 'flatNo', 'email']

    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (  # new fieldset added on to the bottom
            # group heading of your choice; set to None for a blank space instead of a header
            "Verification",
            {
                "fields": ("is_verified", "visible"),
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "is_verified",
                    "flatNo",
                    "password1",
                    "password2",
                    "visible",
                ),
            },
        ),
    )

    inlines = [VehicleInline, ComplaintInline, VisitorInline]


admin.site.register(Resident, ResidentAdmin)
admin.site.register(Vehicle)
admin.site.register(Visitor, VisitorAdmin)
