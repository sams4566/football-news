from django.test import TestCase
from .models import Category
from .forms import CategoryForm

class TestCategoryModel(TestCase):

    def test_category_string_returns_category_name(self):
        category = Category.objects.create(category_name='Test String')
        self.assertEqual(str(category), 'Test String')

    def test_approve_category_defaults_to_false(self):
        category = Category.objects.create(category_name='Test String')
        self.assertFalse(category.approve_category)

class TestCategoryForm(TestCase):

    def test_category_name_is_required(self):
        form = CategoryForm({'category_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['category_name'][0], 'This field is required.')
    