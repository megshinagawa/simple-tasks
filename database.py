import sqlite3

DB_NAME = "tasks.db"

def get_connection():
    """returns a database connection"""
    return sqlite3.connect(DB_NAME)

def init_db():
    """initialize the tasks table in the SQLite database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            task_id TEXT PRIMARY KEY,
            title TEXT NOT NULL, 
            description TEXT,
            category TEXT,
            status TEXT,
            action_date TEXT,
            deadline TEXT,
            estimated_duration INTEGER,
            real_duration INTEGER,
            repeat_status BOOLEAN,
            repeat_frequency TEXT,
            last_updated TEXT
        )
    """)
    conn.commit()
    conn.close()
