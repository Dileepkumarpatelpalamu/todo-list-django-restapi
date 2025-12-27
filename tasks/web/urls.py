from django.urls import path
from .views import (task_list_view,add_task_view,edit_task_view,delete_task_view)

urlpatterns = [
    path("", task_list_view, name="task_list"),
    path("add/", add_task_view, name="add_task"),
    path("edit/<int:task_id>/", edit_task_view, name="edit_task"),
    path("delete/<int:task_id>/", delete_task_view, name="delete_task"),
]
