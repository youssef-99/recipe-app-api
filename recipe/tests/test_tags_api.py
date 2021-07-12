# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from django.test import TestCase
#
# from rest_framework import status
# from rest_framework.test import APIClient
# from recipe.serializers import TagSerialzer
#
# TAG_URL = reverse('recipe:tag-list')
#
#
# class PublicTagsTests(TestCase):
#     """Test the public available tags API"""
#
#     def setUp(self):
#         self.client = APIClient()
#
#     def test_login_required(self):
#         """Test that login is required for retrieving tags"""
#         res = self.client.get(TAG_URL)
#
#         self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
#
#
# class privateTagsApiTests(TestCase):
#     """Test the authorize tags API"""
#
#     def setUp(self):
#         self.user = get_user_model().objects.create()
