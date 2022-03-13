class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user):
        if author in self.books_available:
            if book_name in self.books_available[author]:
                user.books.append(book_name)
                self.books_available[author].remove(book_name)
                if not user.username in self.rented_books.keys():
                    self.rented_books[user.username] = {book_name:days_to_return}
                else:
                    self.rented_books[user.username][book_name] = days_to_return
                return f'{book_name} successfully rented for the next {days_to_return} days!'
            else:
                return f'The book "{book_name}" is already rented and will be available in {self.rented_books[user.username][book_name]} days!'
        return "There is no such author"

    def return_book(self, author, book_name, user):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
        else:
            return f"{user.username} doesn't have this book in his/her records!"

    # def add_user(self, user):
    #     if user in self.user_records:
    #         return f"User with id = {user.user_id} already registered in the library!"
    #     self.user_records.append(user)

    # def remove_user(self, user):
    #     if user in self.user_records:
    #         self.user_records.remove(user)
    #     else:
    #         return f"We could not find such user to remove!"

    # def change_username(self, user_id, new_username):
    #     for user in self.user_records:
    #         if user.user_id == user_id:
    #             if user.username == new_username:
    #                 return f"Please check again the provided username - it should be different than the username used so far!"
    #             else:
    #                 if user.username in self.rented_books.keys():
    #                     self.rented_books[new_username] = self.rented_books[user.username]
    #                     del self.rented_books[user.username]
    #                 user.username = new_username
    #                 return f"Username successfully changed to: {new_username} for userid: {user.user_id}"
    #     return f"There is no user with id = {user_id}!"



