from event_management.enums.budget import Budget
from event_management.enums.city import City
from event_management.enums.event_service import EventService
from event_management.enums.occasion_type import OccasionType
from event_management.purple_fox import PurpleFox
from event_management.services.user_registration import UserRegistration


class EventManagement:
    def __init__(self):
        self.purple_fox = PurpleFox()
        self.user_registration = UserRegistration()

        print("Welcome to PurpleFox Event Management!")
        username = input("Enter username to register: ")
        password = input("Enter password: ")

        is_registered = self.user_registration.register(username, password)
        if is_registered:
            print("Registration successful!")
        else:
            print("Registration failed. Please try again with valid credentials.")
            return
        print("Select a city for your event from the following options:")
        for city in list(City):
            print("- {}".format(city.name))
        city_choice = input("Enter your choice: ")
        selected_city = City[city_choice.upper()]
        self.purple_fox.select_city_for_venue(selected_city)

        print("Select the type of event from the following options:")
        for occasion in list(OccasionType):
            print("- {}".format(occasion.name))
        occasion_choice = input("Enter your choice: ")
        selected_occasion = OccasionType[occasion_choice.upper()]
        self.purple_fox.select_occasion_type(selected_occasion)

        print("Select services for your event from the following options:")
        for event in list(EventService):
            print("- {}".format(event.name))
        event_choice = input("Enter your choice: ")
        selected_event = EventService[event_choice.upper()]
        self.purple_fox.select_service(selected_event)

        print("Select a budget preference from the following options:")
        for budget in list(Budget):
            print("- {}".format(budget.name))
        budget_choice = input("Enter your choice: ")
        selected_budget = Budget[budget_choice.upper()]
        self.purple_fox.select_budget(selected_budget)

        print("\nEvent Summary:")
        print("City: " + self.purple_fox.get_selected_city().name)
        print("Occasion: " + self.purple_fox.get_occasion_type().name)
        print("Services: " + str(self.__convert_selected_service_to_list()))
        print("Budget: " + self.purple_fox.get_selected_budget().name)
        print("Thank you for using PurpleFox!")

    def __convert_selected_service_to_list(self):
        selected_service = list(self.purple_fox.get_selected_service())
        converted_list = [i.name for i in selected_service]
        return converted_list


if __name__ == '__main__':
    EventManagement()
