import requests
from django.shortcuts import render, redirect
from django.contrib import messages

API_BASE = "http://127.0.0.1:8000/api/tasks/"

def task_list_view(request):
    response = requests.get(API_BASE)
    tasks = response.json().get("tasks", [])
    return render(request, "tasks/task_list.html", {"tasks": tasks})
def add_task_view(request):
    if request.method == "POST":
        payload = {
            "title": request.POST["title"],
            "description": request.POST.get("description", ""),
            "due_date": request.POST.get("due_date"),
            "status": "pending",
        }
        response = requests.post(API_BASE, json=payload)
        if response.status_code == 201:
            messages.success(request, "Task added successfully")
        else:
            messages.error(request, "Failed to add task")
        return redirect("task_list")
    return render(request, "tasks/add_task.html")
def edit_task_view(request, task_id):
    response = requests.get(API_BASE)
    tasks = response.json().get("tasks", [])
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        messages.error(request, "❌ Task not found")
        return redirect("task_list")
    if task.get("due_date"):
        task["due_date"] = str(task["due_date"])[:10]
    if request.method == "POST":
        payload = {
            "title": request.POST["title"],
            "description": request.POST.get("description", ""),
            "due_date": request.POST.get("due_date"),
            "status": request.POST.get("status"),
        }
        response = requests.put(f"{API_BASE}{task_id}/", json=payload)
        if response.status_code == 200:
            messages.success(request, "Task updated successfully")
        else:
            messages.error(request, "Failed to update task")
        return redirect("task_list")

    return render(request, "tasks/edit_task.html", {"task": task})
def delete_task_view(request, task_id):
    response = requests.delete(f"{API_BASE}{task_id}/")
    if response.status_code == 200:
        messages.success(request, "Task deleted successfully")
    else:
        messages.error(request, "Failed to delete task")
    return redirect("task_list")
