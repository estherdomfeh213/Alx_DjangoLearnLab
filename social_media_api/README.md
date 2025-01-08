# Social Media API - User Authentication

## Project Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/estherdomfeh213/social_media_api.git
   cd social_media_api


To effectively document the API endpoints for posts and comments, you can provide detailed descriptions, including the required HTTP methods, request and response formats, and any necessary parameters.

### **API Documentation for Posts and Comments**


#### **POST /api/posts/**
- **Description**: Create a new post.
- **Request Body**:
    ```json
    {
        "title": "Post title",
        "content": "Post content",
        "author": "user_id"  // (This will be automatically set to the logged-in user.)
    }
    ```
- **Response**:
    - **201 Created** (on success):
    ```json
    {
        "id": 1,
        "author": "user_id",
        "title": "Post title",
        "content": "Post content",
        "created_at": "2025-01-08T12:00:00Z",
        "updated_at": "2025-01-08T12:00:00Z",
        "comments": []  // Empty array initially
    }
    ```
- **Errors**:
    - **400 Bad Request**: If required fields are missing or invalid.

---

#### **GET /api/posts/**
- **Description**: List all posts with pagination.
- **Response**:
    ```json
    {
        "count": 10,
        "next": "http://localhost:8000/api/posts/?page=2",
        "previous": null,
        "results": [
            {
                "id": 1,
                "author": "user_id",
                "title": "Post title",
                "content": "Post content",
                "created_at": "2025-01-08T12:00:00Z",
                "updated_at": "2025-01-08T12:00:00Z",
                "comments": []
            }
        ]
    }
    ```
- **Pagination**: Responses are paginated with 10 posts per page by default. Use `next` and `previous` links to navigate.

---

#### **GET /api/posts/{id}/**
- **Description**: Retrieve a specific post by ID.
- **Response**:
    ```json
    {
        "id": 1,
        "author": "user_id",
        "title": "Post title",
        "content": "Post content",
        "created_at": "2025-01-08T12:00:00Z",
        "updated_at": "2025-01-08T12:00:00Z",
        "comments": [
            {
                "id": 1,
                "author": "user_id",
                "content": "Comment content",
                "created_at": "2025-01-08T12:05:00Z",
                "updated_at": "2025-01-08T12:05:00Z"
            }
        ]
    }
    ```

---

#### **PUT /api/posts/{id}/**
- **Description**: Update a specific post by ID.
- **Request Body**:
    ```json
    {
        "title": "Updated post title",
        "content": "Updated post content"
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "author": "user_id",
        "title": "Updated post title",
        "content": "Updated post content",
        "created_at": "2025-01-08T12:00:00Z",
        "updated_at": "2025-01-08T12:15:00Z",
        "comments": []
    }
    ```

---

#### **DELETE /api/posts/{id}/**
- **Description**: Delete a specific post by ID.
- **Response**:
    - **204 No Content** (on success).
    - **404 Not Found** (if the post does not exist).

---

#### **POST /api/posts/{id}/add_comment/**
- **Description**: Add a comment to a post.
- **Request Body**:
    ```json
    {
        "content": "Comment content"
    }
    ```
- **Response**:
    - **201 Created** (on success):
    ```json
    {
        "id": 1,
        "post": 1,
        "author": "user_id",
        "content": "Comment content",
        "created_at": "2025-01-08T12:05:00Z",
        "updated_at": "2025-01-08T12:05:00Z"
    }
    ```
- **Errors**:
    - **400 Bad Request**: If the comment content is empty or invalid.

---

#### **GET /api/comments/**
- **Description**: List all comments (supports pagination).
- **Response**:
    ```json
    {
        "count": 5,
        "next": "http://localhost:8000/api/comments/?page=2",
        "previous": null,
        "results": [
            {
                "id": 1,
                "post": 1,
                "author": "user_id",
                "content": "Comment content",
                "created_at": "2025-01-08T12:05:00Z",
                "updated_at": "2025-01-08T12:05:00Z"
            }
        ]
    }
    ```

---

### **Common Error Codes**
- **400 Bad Request**: If the request body is malformed or missing required fields.
- **401 Unauthorized**: If the user is not authenticated.
- **403 Forbidden**: If the user does not have permission to perform the action (e.g., trying to edit a post or comment that doesn’t belong to them).
- **404 Not Found**: If the requested post or comment does not exist.

---

### **Notes:**
- **Authentication**: All endpoints require authentication, and users will need to include their tokens in the `Authorization` header as `Token <token_value>`.
- **Permissions**: Users can only modify or delete their own posts and comments.

---

### **Testing Instructions**:
- You can use Postman to test each endpoint, sending the necessary `Authorization` token in the headers for each request.



1. Follow a User
Endpoint: /follow/<int:user_id>/
Method: POST
Description: Allows a user to follow another user.
Request Example:
http
Copy code
POST /follow/5/
Request Body:
json
Copy code
{
  "user_id": 5
}
Response Example:
json
Copy code
{
  "message": "Successfully followed user 5."
}
Error Response (User already followed):
json
Copy code
{
  "error": "You are already following this user."
}
2. Unfollow a User
Endpoint: /unfollow/<int:user_id>/
Method: POST
Description: Allows a user to unfollow another user.
Request Example:
http
Copy code
POST /unfollow/5/
Request Body:
json
Copy code
{
  "user_id": 5
}
Response Example:
json
Copy code
{
  "message": "Successfully unfollowed user 5."
}
Error Response (User not followed):
json
Copy code
{
  "error": "You are not following this user."
}