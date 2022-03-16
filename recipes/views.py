from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')

def recipe(request, id):
    return render(request, 'recipes/recipe.html')
