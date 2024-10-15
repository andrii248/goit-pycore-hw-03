# Task 4

from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Andy Ukr", "birthday": "1991.11.28"},
    {"name": "Tiberius Shelestak", "birthday": "1987.10.17"},
    {"name": "Evander Holyfield", "birthday": "1962.10.19"},
    {"name": "Snoop Dogg", "birthday": "1962.10.20"},
]


def get_upcoming_birthdays(list_of_users: list) -> list:
    results = []
    today = datetime.today().date()
    current_year = today.year
    for user in list_of_users:
        date_of_birth = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = date_of_birth.replace(year=current_year)

        days_delta = (birthday_this_year - today).days
        congratulation_date = birthday_this_year
        if 0 <= days_delta <= 7:
            weekday = birthday_this_year.weekday()
            if weekday == 5:
                congratulation_date += timedelta(days=2)
            if weekday == 6:
                congratulation_date += timedelta(days=1)
            results.append(
                {"name": user["name"], "congratulation_date": f"{congratulation_date}"}
            )

    return results


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
