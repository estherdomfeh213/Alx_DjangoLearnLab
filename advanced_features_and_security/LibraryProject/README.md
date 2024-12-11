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

## Managing Permissions and Groups

This application uses Django's permissions and groups system for access control.

### Groups and Permissions:

- **Editors:** Can edit and create articles.
- **Viewers:** Can view articles only.
- **Admins:** Have full access to all article actions.

### How to Add Permissions:

1. Navigate to Django Admin -> Groups.
2. Assign the appropriate permissions to each group.

### Enforcing Permissions:

Permissions are enforced using decorators like `@permission_required`. For example:

```python
@permission_required('app_name.can_edit', raise_exception=True)
```
