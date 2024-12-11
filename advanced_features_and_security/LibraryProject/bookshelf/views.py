from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Article  # Import your model
from .models import Book

# Create your views here.
# Create groups

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request):
    # Logic for editing
    return render(request, 'edit_template.html')
  

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'bookshelf/book_list.html', {'books': books})

 
editors_group, _ = Group.objects.get_or_create(name="Editors")
viewers_group, _ = Group.objects.get_or_create(name="Viewers")
admins_group, _ = Group.objects.get_or_create(name="Admins")

# Assign permissions
content_type = ContentType.objects.get_for_model(Article)
permissions = Permission.objects.filter(content_type=content_type)

editors_group.permissions.set(permissions.filter(codename__in=["can_edit", "can_create"]))
viewers_group.permissions.set(permissions.filter(codename="can_view"))
admins_group.permissions.set(permissions)


@permission_required('app_name.can_edit', raise_exception=True)
def edit_article(request, article_id):
    # Logic for editing an article
    return render(request, 'edit_article.html', {})
