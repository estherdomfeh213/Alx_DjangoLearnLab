from django.db import models

# Create your models here.
from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title



# The Author model represents an author in the database.
# Each Author can be linked to multiple books.

# The Book model represents a book authored by an Author.
# The `author` field establishes a one-to-many relationship with the Author model.
