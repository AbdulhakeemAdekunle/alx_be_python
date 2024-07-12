import datetime
from datetime import timedelta

def display_current_datetime():
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d, %H:%M:%S")
    print("Current date and time:", current_date)
display_current_date()

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.date.today()
    number_of_days = timedelta(days=number_of_days)
    future_date = current_date + number_of_days
    print("Future date:", future_date)
calculate_future_date()
