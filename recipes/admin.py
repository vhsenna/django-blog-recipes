from django.contrib import admin
from .models import Category, Recipe

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    searchfields = ['__all__']

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_published', 'category', 'author')
    list_filter = ('is_published', 'created_at', 'updated_at', 'author')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'updated_at'
    ordering = ('is_published', 'updated_at')
    searchfields = ['__all__']
