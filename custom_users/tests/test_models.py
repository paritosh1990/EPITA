from django.test import TestCase
from django.template.defaultfilters import slugify

from custom_users.models import CustomUser


class CustomUserTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email="test@test.dk",
                                                   name="test test",
                                                   password="test")

    def test_user_creation(self):
        user = self.user

        self.assertTrue(isinstance(user, CustomUser))
        self.assertEquals(user.__unicode__(), user.email)
        self.assertEquals(user.get_full_name(), user.name)
        self.assertEquals(user.get_short_name(), user.email)
        self.assertEquals(user.slug, slugify(user.name))

    def test_custom_slug(self):
        user = CustomUser.objects.create_user(email="test2@test2.dk",
                                              name="test test",
                                              password="test",
                                              slug="testing-this-shit!")

        self.assertNotEquals(user.slug, slugify(user.name))
        self.assertEquals(user.slug, "testing-this-shit!")

