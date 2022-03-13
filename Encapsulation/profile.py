class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        else:
            self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.is_long_enough(value) and self.is_upper(value) and self.is_has_digit(value):
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def is_long_enough(self,passw):
        return len(passw) >= 8

    def is_upper(self, passw):
        upper_chars = [ch for ch in passw if ch.isupper()]
        return len(upper_chars) > 0

    def is_has_digit(self, passw):
        digits = [ch for ch in passw if ch.isdigit()]
        return len(digits) > 0

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(self.password)}"



#profile_with_invalid_password = Profile('My_username', 'My-password')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)