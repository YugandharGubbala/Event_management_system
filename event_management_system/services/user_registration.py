class UserRegistration:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username == "" or password == "" or username in self.users.keys():
            return False

        self.users[username] = password
        return True
