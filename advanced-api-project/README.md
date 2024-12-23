BookCreatView: 
# This view allows authenticated users to add new books.
# It validates the publication year to ensure correctness.


## API Endpoints

### Books
- `GET /books/` - List all books
- `GET /books/<int:pk>/` - Retrieve a specific book by ID
- `POST /books/create/` - Create a new book (Authenticated users only)
- `PUT /books/<int:pk>/update/` - Update a book (Authenticated users only)
- `DELETE /books/<int:pk>/delete/` - Delete a book (Authenticated users only)



class BookViewSet(viewsets.ModelViewSet):
    """
    The `BookViewSet` handles all the actions related to books in the system. It provides endpoints for:

    - Listing all books (`GET /books/`).
    - Creating a new book (`POST /books/`).
    - Retrieving details of a specific book (`GET /books/{id}/`).
    - Updating an existing book (`PUT /books/{id}/`).
    - Deleting a book (`DELETE /books/{id}/`).

    In addition, this viewset allows users to filter, search, and sort the book data to better meet their needs:

    **Filtering**:
    - `title`: Filter books by their title.
    - `author`: Filter books by the author's name.
    - `publication_year`: Filter books by the year they were published.

    **Searching**:
    - Users can search for books by keywords in either the title or the author name using the `search` query parameter.

    **Ordering**:
    - Users can sort the results by specific fields, such as `title` or `publication_year`. This can be done in ascending or descending order.

    This setup makes it easy to work with large sets of books, giving users the flexibility to narrow down their search or reorder the list according to their preferences.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']
