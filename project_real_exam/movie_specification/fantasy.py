from project_real_exam.movie_specification.movie import Movie
from project_real_exam.user import User


class Fantasy(Movie):
    def __init__(self, title, year, owner, age_restriction):
        super().__init__(title, year, owner, age_restriction=6)
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) == 0:
            raise ValueError(f"The title cannot be empty string!")
        self.__title = value
        
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError(f"Movies weren't made before 1888!")
        self.__year = value
        
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, value):
        if not type(value) is User:
            raise ValueError(f"The owner must be an object of type User!")
        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 6:
            raise ValueError(f"Fantasy movies must be restricted for audience under 6 years!")
        self.__age_restriction = value

    def details(self):
        return f"Fantasy - Title:{self.__title}, Year:{self.__year}, Age restriction:{self.__age_restriction}, Likes:{self.likes}, Owned by:{self.__owner}"