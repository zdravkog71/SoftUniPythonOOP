class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        message = f"Username: {self.username}, Age: {self.age}\nLiked movies:\n"
        if len(self.movies_liked) > 0:
            for movie in self.movies_liked:
                message += f"{movie.details()}\n"
        else:
            message += f"No movies liked.\n"

        message += f"Owned movies:\n"

        if len(self.movies_owned) > 0:
            for movie in self.movies_owned:
                message += f"{movie.details()}\n"
        else:
            message += f"No movies owned."

        return message