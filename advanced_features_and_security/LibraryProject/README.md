This an introduction to djang Library Project 



## Permissions and Groups Setup

- **Permissions**:
  - `can_view`: Allows viewing of items.
  - `can_create`: Allows creating of items.
  - `can_edit`: Allows editing of items.
  - `can_delete`: Allows deleting of items.

- **Groups**:
  - **Viewers**: Assigned `can_view`.
  - **Editors**: Assigned `can_create` and `can_edit`.
  - **Admins**: Assigned all permissions.

## Testing
1. Create users and assign them to the groups.
2. Verify access based on permissions.
