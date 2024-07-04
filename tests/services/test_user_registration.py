import unittest

from event_management.services.user_registration import UserRegistration


class TestUserRegistration(unittest.TestCase):
    def test_should_return_true_if_user_is_registered(self):
        userRegistration = UserRegistration()

        isUserRegistered = userRegistration.register("Aditya", "Aditya369")

        self.assertTrue(isUserRegistered)

    def test_should_return_false_if_user_is_registered(self):
        userRegistration = UserRegistration()

        isUserRegistered = userRegistration.register("Aditya", "")

        self.assertFalse(isUserRegistered)
