from django.shortcuts import render 
from relationship_app.models import Book, Library
from django.views.generic.detail import DetailView
# Create your views here.
def list_books(request):
  books= Book.objects.all()
  return render(request, 'relationship_app/list_books.html', {'books': books})



class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'