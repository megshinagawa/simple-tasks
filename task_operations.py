from task import Task
from database import get_connection

def add_task(task: Task) -> None:
    """adds a task object to the database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task_id, title, description, category,"
                    "status, action_date, deadline, estimated_duration, real_duration,"
                    "repeat_status, repeat_frequency, last_updated) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (task.task_id, task.title, task.description,task.category,
                    task.status, task.action_date, task.deadline, task.estimated_duration, task.real_duration,
                    task.repeat, task.repeat_frequency, task.last_updated))
    conn.commit()
    conn.close()

def get_all_tasks():
    """Retrieves all tasks from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return [Task(title=row[1], description=row[2], status=row[3], deadline=row[4]) for row in tasks]

def get_task_by_id(task_id):
    pass

def update_task(task_id, title=None, description=None, status=None, due_date=None):
    pass

def delete_task(task_id):
    """deletes a task by its ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
