import os
import time
from datetime import datetime, date, timedelta
import calendar


def get_us_holiday(dt):
    """Return a holiday greeting string if dt is a standard Federal US 
    holiday, otherwise return None."""
    y = dt.year
    
    # Fixed-date US Federal Holidays
    fixed_holidays = {
        (1, 1): "Happy New Year!",
        (6, 19): "Happy Juneteenth!",
        (7, 4): "Happy Independence Day!",
        (11, 11): "Happy Veterans Day!",
        (12, 25): "Merry Christmas!"
    }
    if (dt.month, dt.day) in fixed_holidays:
        return fixed_holidays[(dt.month, dt.day)]

    ### Handle Movable Holidays
    
    # Set calendar
    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    
    ### MLK Day
    # Build List of Mondays in January
    jan_mondays = [d for d in c.itermonthdates(y, 1) if d.month == 1 and \
                   d.weekday() == 0]
    # check if 3rd Monday in Jan
    mlk_day = jan_mondays[2]
    if dt == mlk_day:
        return "Happy Martin Luther King Day!"

    ### Presidents Day
    # Build List of Mondays in January
    feb_mondays = [d for d in c.itermonthdates(y, 2) if d.month == 2 and \
                   d.weekday() == 0]
    # check if 3rd Monday in feb
    pres_day = feb_mondays[2]
    if dt == pres_day:
        return "Happy Presidents Day!"

    # Memorial Day: 
    # Build LIst of Mondays in May
    may_mondays = [d for d in c.itermonthdates(y, 5) if d.month == 5 and \
                   d.weekday() == 0]
    # check if last Monday in May
    memorial_day = may_mondays[-1]
    if dt == memorial_day:
        return "Happy Memorial Day!"

    ### Labor Day
    # Build List of Mondays in September
    sept_mondays = [d for d in c.itermonthdates(y, 9) if d.month == 9 and \
                    d.weekday() == 0]
    labor_day = sept_mondays[0]
    # Check if first Monday in September
    if dt == labor_day:
        return "Happy Labor Day!"
    
    ### Columbus/Indigenous Peoples Day
    # Build List of Mondays in October
    oct_mondays = [d for d in c.itermonthdates(y, 10) if d.month == 10 and \
                    d.weekday() == 0]
    columbus_day = oct_mondays[1]
    # Check if 2nd Monday in September
    if dt == columbus_day:
        return "Happy Columbus or Indigenous Peoples Day!"

    # Thanksgiving: 4th Thursday of November
    # Build List of Thursdays in November
    nov_thursdays = [d for d in c.itermonthdates(y, 11) if d.month == 11 and \
                     d.weekday() == 3]
    thanksgiving = nov_thursdays[3]
    if dt == thanksgiving:
        return "Happy Thanksgiving!"

    ### No Holiday 
    return None


def build_greeting(name):
    """Construct the greeting string with date and holiday logic."""
    # Get Date and Time
    now = datetime.now()
    
    # Set written Day Name
    day_of_week = now.strftime("%A")
    
    # Set written Month Name
    month_name = now.strftime("%B")
    
    # Set date 
    day_of_month = now.day

    # Set Hour
    hour_of_day = now.hour
    
    # Determine Opening:
    if hour_of_day >= 5 and hour_of_day < 10:
        opening = "Good morning, "
    elif hour_of_day >= 12 and hour_of_day <= 17:
        opening = "Good afternoon, "
    elif hour_of_day >= 21 and hour_of_day <= 23:
        opening = "Good evening, "    
    else:
        opening = "Hello, "
        


    # Create Standard Greeting
    greeting = f"{opening}{name}! It's {day_of_week}, {month_name} {day_of_month}."
    
    # Check for holiday
    holiday_greeting = get_us_holiday(now.date())
    if holiday_greeting:
        greeting += " " + holiday_greeting
    
    return greeting


### Setup Folder and Text File upon initial run of program
def main():
    # Set Folder Name
    folder = "Greet Folder"
    file_path = os.path.join(folder, "greeting.txt")

    # Ensure the folder exists, create if needed
    os.makedirs(folder, exist_ok=True)

    # Ensure greeting.txt file exists, create blank greeting.txt file
    with open(file_path, "w") as f:
        f.write("")

    # System Message
    print(f"Watching '{file_path}' for updates...")


    # ---------- Main loop ----------
    # initialize text to ignore
    last_text = ""
    while True:
        try:
            with open(file_path, "r") as f:
                text = f.read().strip()
        except FileNotFoundError:
            text = ""

        if text and text != last_text:
            name = text
            greeting = build_greeting(name)
            with open(file_path, "w") as f:
                f.write(greeting)
            print(f"Updated greeting for '{name}'.")
            last_text = greeting

        # time.sleep(1)  # small delay to lower resource usage

if __name__ == "__main__":
    main()