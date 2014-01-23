from django.contrib import admin
from teaching.models import Course, Content, ReadingListItem, HomeWork

class ContentInline(admin.TabularInline):
    model = Content
    extra = 0

class HomeWorkInline(admin.TabularInline):
    model = HomeWork
    extra = 0

class ReadingListInline(admin.TabularInline):
    model = ReadingListItem
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['start_date', 'end_date'], 'classes': ['collapse']}),
        ('Details', {'fields': ['description', 'url', 'slug', 'code', 'keywords', 'endnote'], 'classes': ['collapse']}),
    ]
    inlines = [ContentInline, HomeWorkInline, ReadingListInline]
    list_display = ('title', 'start_date')
    list_filter = ['start_date']
    search_fields = ['description']

admin.site.register(Course, CourseAdmin)
