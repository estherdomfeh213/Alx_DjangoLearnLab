# Retrieve Operation

Command:
from bookshelf.models import Book
books = Book.objects.get(id=1)
for book in books:
print(book)

Output:
1984 by George Orwell (1949)
