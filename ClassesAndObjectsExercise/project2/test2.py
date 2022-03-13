from ClassesAndObjectsExercise.project.library import Library
from ClassesAndObjectsExercise.project.user import User

user = User(12, 'Valentina')
library = Library()
# library.books_available.update({'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
#                                                              'Harry Potter and the Philosopher\'s Stone',
#                                                              'Harry Potter and the Deathly Hallows',
#                                                              'Harry Potter and the Order of the Phoenix']})
# result = library.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 17, user)
# print(result)
# print(user.books)
# print(library.rented_books)
#print(library.books_available)

library.books_available.update({'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
                                                             'Harry Potter and the Philosopher\'s Stone',
                                                             'Harry Potter and the Deathly Hallows',
                                                             'Harry Potter and the Order of the Phoenix']})
library.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 17, user)
second_user = User(13, 'Peter')
result = library.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 17, user)
print(result)
print(user.books)
print(second_user.books)
print(library.rented_books)
print(library.books_available)
