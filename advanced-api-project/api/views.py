from django_filters.rest_framework import DjangoFilterBackend
#from django_filters import rest_framework as filters
from rest_framework import filters
from rest_framework import viewsets
from django.core.exceptions import ValidationError
from rest_framework import generics 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author'] 
    ordering_fields = ['title', 'publication_year']  
    ordering = ['title'] 
    
    def perform_create(self,serializer):
      publication_year = serializer.validated_data.get('publication_year')
      if publication_year > 2024:
        raise ValidationError("Publication year cannot be in the future")
      serializer.save()
      
# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    

# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self,serializer):
      if 'title' in serializer.validated_data:
        raise ValidationError("The title field cannot be updated.")
      serializer.save()

# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
