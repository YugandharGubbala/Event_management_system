import unittest

from event_management.enums.budget import Budget
from event_management.enums.city import City
from event_management.enums.event_service import EventService
from event_management.enums.occasion_type import OccasionType
from event_management.purple_fox import PurpleFox


class TestPurpleFox(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.purple_fox = PurpleFox()

    def test_user_registration_return_true_if_user_is_registered(self):
        is_user_registered = self.purple_fox.register_user("Aditya", "Aditya369")

        self.assertTrue(is_user_registered)

    def test_select_occasion_type(self):
        self.purple_fox.select_occasion_type(OccasionType.WEDDING)

        occasion_type = self.purple_fox.get_occasion_type()

        self.assertEqual(OccasionType.WEDDING, occasion_type)

    def test_selected_city_for_venue(self):
        self.purple_fox.select_city_for_venue(City.COIMBATORE)

        selected_city = self.purple_fox.get_selected_city()

        self.assertEqual(City.COIMBATORE, selected_city)

    def test_select_service(self):
        self.purple_fox.select_service(EventService.PHOTOGRAPHY)

        selected_services = self.purple_fox.get_selected_service()

        self.assertEqual({EventService.PHOTOGRAPHY}, selected_services)

        self.purple_fox.select_service(EventService.FOOD_CATERING)
        selected_services = self.purple_fox.get_selected_service()

        self.assertEqual({EventService.PHOTOGRAPHY, EventService.FOOD_CATERING}, selected_services)

    def test_select_budget(self):
        self.purple_fox.select_budget(Budget.PREMIUM)

        selected_budget = self.purple_fox.get_selected_budget()

        self.assertEqual(Budget.PREMIUM, selected_budget)
