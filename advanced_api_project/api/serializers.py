from rest_framework import serializers
from .models import Author, Book

#* BookSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

#*AuthorSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']


#! SERIALIZER DOCUMENTATION 

# The BookSerializer serializes all fields of the Book model.
# Includes custom validation to ensure `publication_year` is not in the future.

# The AuthorSerializer serializes the Author model and dynamically includes
# a nested list of books written by the author using BookSerializer.
