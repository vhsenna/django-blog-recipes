from django.contrib import admin
from .models import Category, Recipe

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    searchfields = ['__all__']

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'preparation_time', 'servings', 'created_at', 'updated_at', 'is_published', 'category', 'author')
    searchfields = ['__all__']
