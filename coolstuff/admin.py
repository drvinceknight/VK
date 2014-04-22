from django.contrib import admin

from coolstuff.models import UsefullLink, LettersOfRecommendation, PC, Component

class ContentInline(admin.TabularInline):
    model = Component
    extra = 0

class PCAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
    ]
    inlines = [Component]
    list_display = ('name')

admin.site.register(PC, PCAdmin)
admin.site.register(UsefullLink)
admin.site.register(LettersOfRecommendation)
