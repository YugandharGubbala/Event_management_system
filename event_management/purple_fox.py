from event_management.services.user_registration import UserRegistration


class PurpleFox:
    def __init__(self):
        self.selected_city = None
        self.occasion_type = None
        self.user_registration = UserRegistration()
        self.selected_services = set()

    def register_user(self, username, password):
        return self.user_registration.register(username, password)

    def select_occasion_type(self, occasion_type):
        self.occasion_type = occasion_type

    def get_occasion_type(self):
        return self.occasion_type

    def select_city_for_venue(self, city):
        self.selected_city = city

    def get_selected_city(self):
        return self.selected_city

    def select_service(self, service):
        self.selected_services.add(service)

    def get_selected_service(self):
        return self.selected_services
