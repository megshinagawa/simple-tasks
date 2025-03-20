# cli.py
import argparse
from database import init_db
from task_operations import add_task, get_all_tasks, update_task, delete_task

def main():
    parser = argparse.ArgumentParser(description="Task Management CLI")
    parser.add_argument("action", choices=["add", "list", "update", "delete"], help="Action to perform")
    parser.add_argument("--id", type=int, help="Task ID (for update/delete)")
    parser.add_argument("--title", type=str, help="Title of the task")
    parser.add_argument("--desc", type=str, help="Description of the task")
    parser.add_argument("--status", type=str, choices=["pending", "in-progress", "completed"], help="Task status")
    parser.add_argument("--due", type=str, help="Due date")

    args = parser.parse_args()

    if args.action == "add":
        if args.title:
            add_task(args.title, args.desc, args.status, args.due)
            print("Task added successfully!")
        else:
            print("Error: Title is required for adding a task.")

    elif args.action == "list":
        tasks = get_all_tasks()
        for task in tasks:
            print(task)

    elif args.action == "update":
        if args.id:
            update_task(args.id, args.title, args.desc, args.status, args.due)
            print("Task updated successfully!")
        else:
            print("Task ID is required to update a task.")

    elif args.action == "delete":
        if args.id:
            delete_task(args.id)
            print("Task deleted successfully!")
        else:
            print("Task ID is required to delete a task.")

if __name__ == "__main__":
    init_db()
    main()
