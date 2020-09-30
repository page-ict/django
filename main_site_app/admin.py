from django.contrib import admin
from .models import Post, Resume, Project

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'dob')
    list_filter = ("status",)
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['name', 'content']
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Post, PostAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Project, ProjectAdmin)