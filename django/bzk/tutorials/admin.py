from django.contrib import admin
from .models import Tutorial

# Register your models here.


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published')
    list_filter = ('title', 'published')
    search_fields = ('title','description')
    ordering = ('-published',)






