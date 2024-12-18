from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=255)
  
  def __str__(self):
    return self.name
  
  
class Book(models.Model):
  title = models.CharField(max_length=255)
  publication_year = models.IntegerField()
  author = models.ForeignKey(Author, related_name ='books', on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title 
  
  

"""
Author and Book models:
- Author: Represents a book author with a one-to-many relationship to books.
- Book: Represents a book with details such as title, publication year, and its author.
"""
