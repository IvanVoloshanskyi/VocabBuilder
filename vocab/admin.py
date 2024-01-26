from django.contrib import admin
from vocab.models import Word, Category, RecommendWord


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'en_word',
        'ua_word',
        'category',
        'owner',
        'status',
        'created_at',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'title',


@admin.register(RecommendWord)
class RecommendWordAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'en_word',
        'ua_word',
        'category',
        'created_at',
    )
