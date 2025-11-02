from classes.books.book import Book
from classes.libraries.library import *
from classes.users.user import User



library = Library()
library.add_book(Book("harypoter", "jon", "1968968"))
library.register_user(User("2165658", "Idan"))
library.perform_borrow("2165658", "1968968")
print(library.books["1968968"].isavailable)
library.return_borrow("2165658" ,"1968968")
print(library.books["1968968"].isavailable)