from django.shortcuts import render


def index(request):
    return render(request, 'adminapp/index.html')


# Read
def admin_users(request):
    return render(request, 'adminapp/admin-users-read.html')

# Create
def admin_users_create(request):
    return render(request, 'adminapp/admin-users-create.html')

# Update
def admin_users_update(request):
    return render(request, 'adminapp/admin-users-update-delete.html')

# Delete
def admin_users_delete(request):
    pass