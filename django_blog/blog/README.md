Here’s a suggested structure for documenting the CRUD features in the `README.md`:

---

## **Blog Post Management Features Documentation**

### **Overview**

The Blog Post Management system in the Django blog project allows authenticated users to create, read, update, and delete blog posts (CRUD functionality). This feature ensures that users can manage content dynamically, while also providing proper access control to secure user posts.

Key functionalities include:
- **List Posts**: All blog posts are listed with the option to view full details.
- **View Post**: Each post can be viewed individually with full content.
- **Create Post**: Authenticated users can create new posts. The author field is automatically assigned based on the logged-in user.
- **Edit Post**: Authors can edit their own posts.
- **Delete Post**: Authors can delete their posts. Only the author has permission to delete their own post.

---

### **User Guide**

#### **For Authors**
1. **Creating a Blog Post**
   - Navigate to the “Create Post” page by clicking the “New Post” link from the homepage or the navigation menu.
   - Fill in the post title and content in the form fields.
   - Submit the form to create the post. Once created, the post will be listed on the homepage and other views.
   
2. **Editing a Blog Post**
   - To edit an existing post, click the “Edit” link on the post detail page.
   - Modify the content and title as needed, then submit the form to save the changes.
   
3. **Deleting a Blog Post**
   - If you wish to delete a post, click the “Delete” link on the post detail page.
   - Confirm the deletion to permanently remove the post from the blog.

#### **For Readers**
- Readers can view all blog posts in a list format, where they can see the title and a snippet of the post.
- Clicking on the title of any post will take them to the full post, where they can read its content.

---

### **Testing the Blog Post Features**

#### **Testing Navigation and Views**
1. **Test List View**
   - Ensure the home page (`/`) lists all available posts, with titles and excerpts.
   - Clicking on any post title should navigate to the detailed view for that post.

2. **Test Detail View**
   - Verify that individual post details are accessible at `/posts/<post_id>/` (where `<post_id>` is the ID of the post).
   - Check that the post's full content is displayed.

3. **Test Create Post**
   - Navigate to the “Create Post” page (`/posts/new/`).
   - Ensure the form for title and content is visible.
   - Submit a valid form and verify the post is created, and you are redirected to the post's detail page.

4. **Test Edit Post**
   - Navigate to the “Edit” page (`/posts/<post_id>/edit/`).
   - Ensure that only the post's author can access this page.
   - Edit the post content and verify that the changes are saved.

5. **Test Delete Post**
   - Ensure that only the author of the post can access the delete page (`/posts/<post_id>/delete/`).
   - Attempt to delete a post and verify that it is removed after confirmation.

#### **Testing Permissions and Security**
1. **Authentication**
   - Ensure that only authenticated users can create, edit, or delete posts. Unauthenticated users should be redirected to the login page.
   
2. **Permissions**
   - Ensure that authors can only edit or delete their own posts, not posts created by others. If a user tries to access another user’s post for editing or deletion, they should receive a “Permission Denied” error.
   
3. **CSRF Protection**
   - Test form submissions without a CSRF token to verify that Django’s CSRF protection is working.

4. **General Navigation**
   - Ensure that the navigation between list, detail, create, edit, and delete views is functioning correctly, with no broken links.

