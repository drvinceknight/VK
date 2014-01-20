from django.contrib import admin
from teaching.models import Course, Content

class ContentInline(admin.TabularInline):
    model = Content
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['start_date', 'end_date'], 'classes': ['collapse']}),
        ('Details', {'fields': ['description', 'url', 'slug', 'code', 'keywords'], 'classes': ['collapse']}),
    ]
    inlines = [ContentInline]
    list_display = ('title', 'start_date')
    list_filter = ['start_date']
    search_fields = ['description']

admin.site.register(Course, CourseAdmin)
