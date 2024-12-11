from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

# Create your views here.

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request):
    # Logic for editing
    return render(request, 'edit_template.html')
