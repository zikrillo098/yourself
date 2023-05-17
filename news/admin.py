from django.contrib import admin
from .models import *

admin.site.register(Article)
admin.site.register(Category)


class CategoryList(admin.ModelAdmin):
    list_display_links = ('pk', 'title')
    list_display = ('title', 'pk')

    def get_len(self, obj):
        if obj.article:
            return len(obj.article.all())
        else:
            return '0'

    get_len.short_description = 'Количестко статей в категории'


class GalleryInline(admin.TabularInline):
    fk_name = 'article'
    model = Gallery
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'watched', 'published', 'theme')
    list_display_links = ('title', 'pk')
    list_editable = ('title', 'watched', 'theme')

    fieldsets = ({
        'Главные товары'
    })
