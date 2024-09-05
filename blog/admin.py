from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_filter = ('title', 'tags', 'date')
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'date', 'author')


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)

