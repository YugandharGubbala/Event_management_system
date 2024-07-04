import unittest

from event_management.services.user_registration import UserRegistration


class TestUserRegistration(unittest.TestCase):
    def test_should_return_true_if_user_is_registered(self):
        user_registration = UserRegistration()

        is_user_registered = user_registration.register("Aditya", "Aditya369")

        self.assertTrue(is_user_registered)

    def test_should_return_false_if_user_is_registered(self):
        user_registration = UserRegistration()

        is_user_registered = user_registration.register("Aditya", "")

        self.assertFalse(is_user_registered)
