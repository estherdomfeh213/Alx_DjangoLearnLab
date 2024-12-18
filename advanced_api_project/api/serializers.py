from dataclasses import field
from rest_framework import serializers
from .models import Author, Book
from datetime import date 

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book 
    field = ['id', 'title', 'publuication_year', 'author']
    
  def validate_publication_year(self, value):
    current_year = date.date.today().year
    if value > current_year:
      raise serializers.ValidationError("Publication year cannot be in the future.")
    return value 
  

class AuthorSerializer(serializers.ModelSerializer):
  books = BookSerializer(many=True, read_only=True)
  
  class Meta:
    model = Author
    field = ['id', 'name', 'books']
    
    
    
    
"""
BookSerializer:
- Serializes all fields of the Book model.
- Includes validation to ensure the publication year is not in the future.

AuthorSerializer:
- Serializes the name field of the Author model.
- Includes a nested BookSerializer to serialize related books dynamically.
"""
