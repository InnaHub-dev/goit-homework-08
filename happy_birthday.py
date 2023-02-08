from datetime import datetime

def get_birthdays_per_week(users: dict[str,datetime]) -> dict[str, list[str]]:
    '''Function prints all the birthdays within 7 days from the current date. If the birthday was on the weekend, it moves it to Monday.
    
    Returns a dictionary of birthday guys.'''

    current_day = datetime.now()
    happy_birthday = {}

    for user, date in users.items():
        date = datetime(year=current_day.year, month=date.month, day=date.day)
        difference = date - current_day

        if 0 < difference.days <= 7:
            weekday = date.strftime('%A')

            if weekday =='Saturday':
                weekday = 'Monday'

            if not weekday in happy_birthday.keys():
                happy_birthday.update({weekday:[user]})
            else:
                happy_birthday[weekday].append(user)

    for key, value in happy_birthday.items():
        print(f"{key}: {str(', '.join(value))}")
    
    return happy_birthday
    

def main():
    users = {'Jill':datetime(year=1967, month=1, day=27), 'John':datetime(year=1966, month=2, day=10), 'Ian':datetime(year=1990, month=2, day=10), 'Jim':datetime(year=1966, month=2, day=11)}

    get_birthdays_per_week(users)


if __name__ == '__main__':
    main()

