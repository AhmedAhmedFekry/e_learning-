from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Content, Subject, Course, Module, Text

# use memcache admin index site
admin.site.index_template = 'memcache_status/admin_index.html'

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
class ModuleInline(admin.StackedInline):
    model = Module
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created','price']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
admin.site.register(Content)
admin.site.register(Text)