from StaticAndClassMethodsExercise.projectDVD.customer import Customer
from StaticAndClassMethodsExercise.projectDVD.dvd import DVD
from StaticAndClassMethodsExercise.projectDVD.movie_world import MovieWorld

c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))
#print(c1.__repr__())
#print(d2.is_rented)
print(movie_world)