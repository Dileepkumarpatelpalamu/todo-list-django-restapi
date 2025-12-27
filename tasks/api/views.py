import json
import logging
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tasks.db import (create_task,get_all_tasks,update_task,delete_task)

logger = logging.getLogger(__name__)

ALLOWED_STATUS = ["pending", "completed"]
REQUIRED_FIELDS = ["title", "due_date", "status"]


def parse_json(request):
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return None


def validate_task_data(data):
    # Required fields
    for field in REQUIRED_FIELDS:
        if not data.get(field):
            return f"{field} is required"

    # Status validation
    if data["status"] not in ALLOWED_STATUS:
        return "Status must be 'pending' or 'completed'"

    # Date format validation
    try:
        datetime.strptime(data["due_date"], "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD"

    return None


@csrf_exempt
def tasks_api(request):
    try:
        if request.method == "GET":
            return JsonResponse(
                {"tasks": get_all_tasks()},
                status=200
            )

        if request.method == "POST":
            data = parse_json(request)
            if not data:
                return JsonResponse(
                    {"error": "Invalid JSON payload"},
                    status=400
                )

            error = validate_task_data(data)
            if error:
                return JsonResponse(
                    {"error": error},
                    status=400
                )

            create_task(
                data["title"],
                data.get("description", ""),
                data["due_date"],
                data["status"]
            )

            return JsonResponse(
                {"message": "Task created successfully"},
                status=201
            )

        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    except Exception as e:
        logger.exception("Task API error")
        return JsonResponse(
            {"error": "Internal server error"},
            status=500
        )


@csrf_exempt
def task_detail_api(request, task_id):
    try:
        if request.method == "PUT":
            data = parse_json(request)
            if not data:
                return JsonResponse(
                    {"error": "Invalid JSON payload"},
                    status=400
                )

            error = validate_task_data(data)
            if error:
                return JsonResponse(
                    {"error": error},
                    status=400
                )

            rows = update_task(
                task_id,
                data["title"],
                data.get("description", ""),
                data["due_date"],
                data["status"],
            )

            if rows == 0:
                return JsonResponse(
                    {"error": "Task not found"},
                    status=404
                )

            return JsonResponse(
                {"message": "Task updated successfully"},
                status=200
            )

        if request.method == "DELETE":
            rows = delete_task(task_id)
            if rows == 0:
                return JsonResponse(
                    {"error": "Task not found"},
                    status=404
                )

            return JsonResponse(
                {"message": "Task deleted successfully"},
                status=200
            )

        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )

    except Exception as e:
        logger.exception("Task Detail API error")
        return JsonResponse(
            {"error": "Internal server error"},
            status=500
        )
