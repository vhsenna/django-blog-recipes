from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

class RecipeURLsTest(TestCase):

    def test_recipe_home_url_is_working(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_id_url_is_working(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipe/1/')

    def test_recipe_category_url_is_working(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipe/category/1/')

class RecipeViewsTest(TestCase):

    def test_recipe_home_view_function_is_working(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_id_view_function_is_working(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_category_view_function_is_working(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
