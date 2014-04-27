from django.contrib import admin

from coolstuff.models import UsefullLink, LettersOfRecommendation, PC, Component, MediaAppearance

class ComponentInLine(admin.TabularInline):
    model = Component
    extra = 0

class PCAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
    ]
    inlines = [ComponentInLine]

admin.site.register(LettersOfRecommendation)
admin.site.register(MediaAppearance)
admin.site.register(PC, PCAdmin)
admin.site.register(UsefullLink)
