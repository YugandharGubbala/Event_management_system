from event_management_system.services.user_registration import UserRegistration


class PurpleFox:
    def __init__(self):
        self.__selected_budget = None
        self.__selected_city = None
        self.__occasion_type = None
        self.__user_registration = UserRegistration()
        self.__selected_services = set()

    def register_user(self, username, password):
        return self.__user_registration.register(username, password)

    def select_occasion_type(self, occasion_type):
        self.__occasion_type = occasion_type

    def get_occasion_type(self):
        return self.__occasion_type

    def select_city_for_venue(self, city):
        self.__selected_city = city

    def get_selected_city(self):
        return self.__selected_city

    def select_service(self, service):
        self.__selected_services.add(service)

    def get_selected_service(self):
        return self.__selected_services

    def select_budget(self, budget):
        self.__selected_budget = budget

    def get_selected_budget(self):
        return self.__selected_budget

    def is_service_selected(self, service):
        return service in self.__selected_services
