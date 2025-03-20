import datetime

STATUS_DICT = {
    'pending':' ',
    'in progress':'/',
    'paused':'=',
    'completed':'x',
    'cancelled':'-'
}

def validate_date(date_str: str) -> bool:
    """checks the validity of the date string"""
    if date_str is None:
        return False
    try:
        datetime.date.fromisoformat(date_str)
        return True
    except ValueError:
        return False

def format_minutes(minutes: int) -> str:
    """formats minutes into a 00:00 format string"""
    hours = minutes // 60 
    remainder_minutes = minutes % 60
    return f"{hours:02}:{remainder_minutes:02}"