from django.contrib import admin

# Register your models here.
from blogapp.models import Blog,Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','Description','publish','created','updated','status','Image']
    list_filter = ('status','author','created','publish')
    search_fields = ('title','Description')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug':('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','Description','created','updated','active']
    list_filter = ['active','created','updated']
    search_fields = ('name','email','Description')


admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)