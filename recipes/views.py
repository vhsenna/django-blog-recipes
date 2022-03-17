from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.faker import make_recipe

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'recipes': [make_recipe() for _ in range(13)],
    })

def recipe(request, id):
    return render(request, 'recipes/recipe.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
