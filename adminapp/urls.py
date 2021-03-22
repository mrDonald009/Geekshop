from django.urls import path

from adminapp.views import index, UserListView, UserCreateView, UsersUpdateView, UserDeleteView

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UsersUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),
]