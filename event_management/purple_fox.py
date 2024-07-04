from event_management.services.user_registration import UserRegistration


class PurpleFox:
    def __init__(self):
        self.user_registration = UserRegistration()
        self.selectedServices = {}

    def register_user(self, username, password):
        return self.user_registration.register(username, password)
