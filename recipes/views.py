from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.faker import make_recipe
from recipes.models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/home.html', context={
        'recipes': recipes,
    })

def recipe(request, id):
    return render(request, 'recipes/recipe.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
