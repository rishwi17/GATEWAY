from django.contrib import admin
from .models import Discussion, Reply

# Register your models here.


class ReplyInline(admin.TabularInline):
    model = Reply


class ReplyAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by', "parent")


class DiscussionAdmin(admin.ModelAdmin):
    readonly_fields = ("created_by",)
    inlines = [ReplyInline]


admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Reply, ReplyAdmin)
