# Task

from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        from_today_delta = (today - formatted_date).days
        return from_today_delta
    
    except ValueError: 
        return (f"Ooops! The format of the {date} is incorrect. Please enter in the format YYYY-MM-DD")



print(get_days_from_today("25-01-01"))
print(get_days_from_today("2025-01-01"))
print(get_days_from_today("1991-11-28"))
