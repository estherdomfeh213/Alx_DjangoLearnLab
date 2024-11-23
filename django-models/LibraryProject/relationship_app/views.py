from django.shortcuts import render
from django.views.generic.detail import DetailView 
from relationship_app.models import Book, Library
# Create your views here.
def list_books(request):
  books= Book.objects.select_related('author').all()
  return render(request, 'list_books.html', {'books': books})



class LibraryDetailView(DetailView):
  model = Library
  template_name = 'library_detail.html'
  context_object_name = 'library'