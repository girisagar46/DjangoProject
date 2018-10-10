from django.test import TestCase
from django.contrib.auth.models import User

class UserTest(TestCase):

    def test_create_user(self):
        user_dict = {}
        user_dict["username"] = "test_user"
        user_dict["email"] = "test@test.test"
        User.objects.create(**user_dict)

        users = User.objects.all()
        self.assertEqual(users.count(), 1)
        self.assertEqual(users[0].username, "test_user")