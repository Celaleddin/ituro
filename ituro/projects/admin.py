from django.contrib import admin
from projects.models import Project, Membership


class MembershipInlineAdmin(admin.TabularInline):
    model = Membership


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    inlines = [MembershipInlineAdmin]


admin.site.register(Project, ProjectAdmin)