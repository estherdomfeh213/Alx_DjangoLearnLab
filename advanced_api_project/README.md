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

