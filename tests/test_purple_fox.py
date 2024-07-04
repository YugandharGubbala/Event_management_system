import unittest

from event_management.purple_fox import PurpleFox


class TestPurpleFox(unittest.TestCase):

    def test_user_registration_return_true_if_user_is_registered(self):
        purple_fox = PurpleFox()

        is_user_registered = purple_fox.register_user("Aditya", "Aditya369")

        self.assertTrue(is_user_registered)
