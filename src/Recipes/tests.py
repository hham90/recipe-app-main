from django.test import TestCase
from .models import Recipes

# Create your tests here.
class RecipesModelTest(TestCase):
    def setUpTestData():
        # test object
        Recipes.objects.create(name='Apple Pie', ingredients='Apples, Pie Crust, Sugar', cooking_time='5', difficulty='Easy')

    def test_Recipe_name(self):
       # Get a Recipe object to test
       Recipe = Recipes.objects.get(id=1)

       # Get the metadata for the 'name' field and use it to query its data
       field_label = Recipes._meta.get_field('name').verbose_name

       # Compare the value to the expected result
       self.assertEqual(field_label, 'name')

    def test_author_name_max_length(self):
           # Get a Recipe object to test
           Recipe = Recipes.objects.get(id=1)

           # Get the metadata for the 'name' field and use it to query its max_length
           max_length = Recipes._meta.get_field('name').max_length

           # Compare the value to the expected result i.e. 120
           self.assertEqual(max_length, 120)

    def test_get_absolute_url(self):
       recipe = Recipes.objects.get(id=1)
       #get_absolute_url() should take you to the detail page of Recipe #1
       #and load the URL /list/1
       self.assertEqual(recipe.get_absolute_url(), '/list/1')