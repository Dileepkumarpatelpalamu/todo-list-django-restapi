from django.urls import path
from .views import tasks_api, task_detail_api
urlpatterns = [
     path("tasks/", tasks_api, name="tasks_api"),
    path("tasks/<int:task_id>/", task_detail_api, name="task_detail_api"),
]