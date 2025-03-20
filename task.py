import uuid
from utils import STATUS_DICT, validate_date, format_minutes

class Task:
    def __init__(self, title: str, description: str = None, category: str = "inbox", status: str = 'pending',
                 action_date: str = None, deadline: str = None, estimated_duration: int = 0, real_duration: int = 0,
                 repeat: bool = False, repeat_frequency: str = None) -> None:
        self.task_id = uuid.uuid4().hex
        self.title = title
        self.description = description
        self.category = category
        self.status = status
        self.action_date = action_date if validate_date(action_date) else None
        self.deadline = deadline if validate_date(deadline) else None
        self.estimated_duration = estimated_duration
        self.real_duration = real_duration
        self.repeat = repeat
        self.repeat_frequency = repeat_frequency
        self.last_updated = None

    def __repr__(self) -> str:
        if self.action_date:
            line_01 = f'[{STATUS_DICT[self.status]}] {self.title} ({self.action_date})'
        else:
            line_01 = f'[{STATUS_DICT[self.status]}] {self.title}'
        line_02 = f'    L {self.description}' if self.description else None
        if self.deadline:
            line_03 = f'    L # {self.category}  〆 {self.deadline}  [{format_minutes(self.real_duration)}/{format_minutes(self.estimated_duration)}]'
        else: 
            line_03 = f'    L # {self.category}  〆 ----  [{format_minutes(self.real_duration)}/{format_minutes(self.estimated_duration)}]'
        if line_02 is None:
            return f'{line_01}\n{line_03}'
        return f'{line_01}\n{line_02}\n{line_03}'
    
    @staticmethod
    def get_by_id(task_id):
        """Retrieves a task from the database and returns a Task object."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return Task()
        return None  # No task found

task_01 = Task("hello world", category = "work")
task_02 = Task("test task 02", action_date = "2025-03-20")
task_03 = Task("test task 03", deadline="skdjfdskaj")

print(task_01)
print(task_02)
print(task_03)