from django.test import TestCase
from .models import Category
from .forms import CategoryForm

class TestCategoryModel(TestCase):

    def test_category_string_gives_back_category_name(self):
        category = Category.objects.create(category_name='Test String')
        self.assertEqual(str(category), 'Test String')

    def test_approve_category_set_to_false(self):
        category = Category.objects.create(category_name='Test String')
        self.assertFalse(category.approve_category)

class TestCategoryForm(TestCase):

    def test_category_name_is_needed(self):
        form = CategoryForm({'category_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['category_name'][0], 'This field is required.')

class TestViews(TestCase):

    def test_retrieve_category_list(self):
        page = self.client.get('/categories')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'categories.html')

    def test_retrieve_add_category_html(self):
        page = self.client.get('/category/add')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'add_category.html')

    def test_retrieve_edit_category_html(self):
        category = Category.objects.create(category_name='Test String')
        page = self.client.get(f'/category/edit/{category.id}')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'edit_category.html')

    def test_category_added(self):
        page = self.client.post('/category/add', {'category_name': 'Test String'})
        self.assertRedirects(page, '/categories')
