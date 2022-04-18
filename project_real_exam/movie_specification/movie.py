from abc import ABC, abstractmethod

class Movie(ABC):
    def __init__(self, title, year, owner, age_restriction):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @abstractmethod
    def details(self):
        pass
