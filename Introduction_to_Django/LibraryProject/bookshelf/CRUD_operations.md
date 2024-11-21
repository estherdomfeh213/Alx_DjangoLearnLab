# CRUD Operation in the Django Shell

# Create Operation

Command:
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

Output:
1984 by George Orwell (1949)

# Retrieve Operation

Command:
from bookshelf.models import Book
books = Book.objects.all()
for book in books:
print(book)

Output:
1984 by George Orwell (1949)

# Update Operation

Command:
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(id=book.id)
print(updated_book)

Output:
Nineteen Eighty-Four by George Orwell (1949)

# Delete Operation

Command:
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
books = Book.objects.all()
print(books)

Output:
<QuerySet []>
