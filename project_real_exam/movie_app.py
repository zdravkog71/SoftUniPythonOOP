from project_real_exam.movie_specification.action import Action
from project_real_exam.movie_specification.fantasy import Fantasy
from project_real_exam.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username, age):
        for user in self.users_collection:
            if user.username == username:
                raise Exception(f"User already exists!")
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username, movie):
        # check whether user is registered
        is_user_registered = False
        for user in self.users_collection:
            if user.username == username:
                is_user_registered = True
        if not is_user_registered:
            raise Exception(f"This user does not exist!")

        # check if movie has been allready uploaded
        if movie in self.movies_collection:
            raise Exception(f"Movie already added to the collection!")

        # check owner
        if movie.owner.username == username:
            self.movies_collection.append(movie)
            return f"{username} successfully added {movie.title} movie."
        raise Exception(f"{username} is not the owner of the movie {movie.title}!")

    def edit_movie(self, username, movie, **kwargs):
        if not movie in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not movie.owner.username == username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key,new_value in kwargs.items():
            if key == "title":
                movie.title = new_value
            elif key == "year":
                movie.year = new_value
            else:
                movie.age_restriction = new_value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie):
        if not movie in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not movie.owner.username == username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."


    def like_movie(self, username, movie):
        for user in self.users_collection:
            if user.username == username:
                if movie in user.movies_owned:
                    raise Exception(f"{username} is the owner of the movie {movie.title}!")

        for user in self.users_collection:
            if user.username == username:
                if movie in user.movies_liked:
                    raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1

        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.append(movie)
                return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie):
        # if not movie in username.movies_liked:
        #     raise Exception(f"{username} has not liked the movie {movie.title}!")
        is_movie_liked = False
        for user in self.users_collection:
            if user.username == username:
                if movie in user.movies_liked:
                    is_movie_liked = True
        if not is_movie_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.remove(movie)
                return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda x: x.year, reverse=True)
        message = ""
        for movie in sorted_movies:
            message += f"{movie.details()}\n"
        return message

    def __str__(self):
        message = "All users: "
        if len(self.users_collection) > 0:
            message += ", ".join([u.username for u in self.users_collection])
        else:
            message += "No users."
        message += "\n"
        if len(self.movies_collection) > 0:
            message += ", ".join([m.title for m in self.movies_collection])
        else:
            message += "No movies."

        return message



# movie_app = MovieApp()
# print(movie_app.register_user('Martin', 24))
# user = movie_app.users_collection[0]
# movie = Action('Die Hard', 1988, user, 18)
# print(movie_app.upload_movie('Martin', movie))
# print(movie_app.movies_collection[0].title)
# print(movie_app.register_user('Alexandra', 25))
# user2 = movie_app.users_collection[1]
# movie2 = Action('Free Guy', 2021, user2, 16)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.like_movie('Alexandra', movie))
# print(movie_app.dislike_movie('Martin', movie2))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.delete_movie('Alexandra', movie2))
# movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.display_movies())
# print(movie_app)