from django.db import connection
def create_task(title, description, due_date, status):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO tasks_task (title, description, due_date, status)
            VALUES (%s, %s, %s, %s)
            """,
            [title, description, due_date, status]
        )

def get_all_tasks():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, title, description, due_date, status FROM tasks_task"
        )
        rows = cursor.fetchall()

    return [
        {
            "id": r[0],
            "title": r[1],
            "description": r[2],
            "due_date": r[3],
            "status": r[4],
        }
        for r in rows
    ]

def update_task(task_id, title, description, due_date, status):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE tasks_task
            SET title=%s, description=%s, due_date=%s, status=%s
            WHERE id=%s
            """,
            [title, description, due_date, status, task_id]
        )
        return cursor.rowcount

def delete_task(task_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM tasks_task WHERE id=%s",
            [task_id]
        )
        return cursor.rowcount