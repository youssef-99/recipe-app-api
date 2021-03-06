from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user():
    return get_user_model().objects.create_user(email='test@test.com', password='123456')


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@test.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email, '123456')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123456')

    def test_create_super_user(self):
        """Test creat new super user"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            '123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredients = models.Ingredients.objects.create(
            user=sample_user(),
            name='Cucumber'
        )
        self.assertEqual(str(ingredients), ingredients.name)
