from datetime import datetime


def get_time():
    current_time = datetime.now()
    weekday_name = current_time.strftime("%A")
    return f"Today is {weekday_name}: {current_time.strftime('%B')} {current_time.day}, {current_time.year}."


print(get_time())


parsed_bday = datetime.strptime("Aug 30, 1992", "%b %d, %Y")
parsed_bday_date = parsed_bday.date()
bday_weekday = parsed_bday_date.strftime("%A")
bday_month = parsed_bday_date.strftime("%B")
bday_day = parsed_bday_date.strftime("%d")
bday_year = parsed_bday_date.strftime("%Y")

print(f"\n My Birthday was {bday_weekday}: {bday_month} {bday_day}, {bday_year}.")

date_string = datetime.strftime(datetime.now(), "%a %b/%d/%Y")

age = datetime.now() - parsed_bday
days_old = age.days
years_old = int(days_old) / 365


print(f"I am {int(years_old)} years old. I have lived for {days_old} days.")
