from django.shortcuts import render, get_list_or_404
from utils.recipes.faker import make_recipe
from recipes.models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')

    return render(request, 'recipes/home.html', context={
        'recipes': recipes,
    })

def recipe(request, id):
    recipe = Recipe.objects.filter(
        pk=id,
        is_published=True,
    ).order_by('-id').first()

    return render(request, 'recipes/recipe.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })

def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
        ).order_by('-id')
    )

    return render(request, 'recipes/home.html', context={
        'recipes': recipes,
    })
