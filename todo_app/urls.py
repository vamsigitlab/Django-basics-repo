from django.urls import path
from todo_app import views

urlpatterns = [
    path('list/', views.list_view, name="todo_list_view"),
    path('create/', views.create_view, name="todo_create_view"),
    path('update/<int:todo_id>', views.update_view, name="todo_update_view"),
    path('delete/<int:todo_id>', views.delete_view, name="todo_delete_view"),
]
