# In forms.py
from django import forms

class BookForm(forms.Form):
    name = forms.CharField(max_length=255)
    author = forms.CharField(max_length=255)

# In views.py
from .forms import BookForm

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Process the data safely
            pass
