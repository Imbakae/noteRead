from django.contrib import admin

# Register your models here.
from note.models import BlogArticles


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)

    ordering = ["-publish", "author"]


admin.site.register(BlogArticles, BlogArticlesAdmin)
