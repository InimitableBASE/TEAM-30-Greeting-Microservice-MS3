'''
This program imports build_greeting from greeting.py and mocks a time/date to 
test that the proper greeting output based on the time of day and day of the 
year. IT IS NOT USED AS A TEST CALL TO THE MICROSERVICE - for that, see the 
file _testGreeting.py 
'''

from greeting import build_greeting
from unittest.mock import patch
from datetime import datetime


def main():
    
    ### TEST CASES
    # Test Cases for Time of Day
    date = datetime.now()
    yr = date.year
    month = date.month
    day = date.day



    print(f"\nTESTING 4:59 AM WITH NAME: BUGS BUNNY:")
    hr = 4
    min = 59
    name = 'Bugs Bunny'
    fake_now = datetime(yr, month, day, hr, min, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING 5:00 AM WITH NAME: BUGS BUNNY:")
    hr = 5
    min = 0
    name = 'Bugs Bunny'
    fake_now = datetime(yr, month, day, hr, min, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING 9:59 AM WITH NAME: BUGS BUNNY:")
    hr = 9
    min = 59
    name = 'Bugs Bunny'
    fake_now = datetime(yr, month, day, hr, min, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))
    
    print(f"\nTESTING 10:00 AM WITH NAME: BUGS BUNNY:")
    hr = 10
    min = 0
    name = 'Bugs Bunny'
    fake_now = datetime(yr, month, day, hr, min, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING 11:59 PM WITH NAME: BUGS BUNNY:")
    hr = 11
    min = 59
    name = 'Bugs Bunny'
    fake_now = datetime(yr, month, day, hr, min, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))
    
    print(f"\nTESTING 12:00 PM WITH NAME: BUGS BUNNY:")
    hr = 12
    min = 00
    name = 'Bugs Bunny'
    fake_now = datetime(yr, month, day, hr, min, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING 5:59 PM WITH NAME: BUGS BUNNY:")
    hr = 17
    min = 59
    name = 'Bugs Bunny'
    fake_now = datetime(yr, month, day, hr, min, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING 6:00 PM WITH NAME: BUGS BUNNY:")
    hr = 18
    min = 00
    name = 'Bugs Bunny'
    fake_now = datetime(yr, month, day, hr, min, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING 8:59 PM WITH NAME: BUGS BUNNY:")
    hr = 20
    min = 59
    name = 'Bugs Bunny'
    fake_now = datetime(yr, month, day, hr, min, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING 9:00 PM WITH NAME: BUGS BUNNY:")
    hr = 21
    min = 00
    name = 'Bugs Bunny'
    fake_now = datetime(yr, month, day, hr, min, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING 11:59 PM WITH NAME: BUGS BUNNY:")
    hr = 23
    min = 59
    name = 'Bugs Bunny'
    fake_now = datetime(yr, month, day, hr, min, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING 12:00 AM WITH NAME: BUGS BUNNY:")
    hr = 0
    min = 0
    name = 'Bugs Bunny'
    fake_now = datetime(yr, month, day, hr, min, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))


    # Test Cases for Holidays
    print(f"\nTESTING NEW YEARS DAY 12:30 AM WITH NAME: BUGS BUNNY:")
    fake_now = datetime(2026, 1, 1, 0, 30, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING MLK DAY 10:00 AM WITH NAME: BUGS BUNNY:")
    fake_now = datetime(2026, 1, 19, 10, 0, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING PRESIDENTS DAY 12:30 PM WITH NAME: BUGS BUNNY:")
    fake_now = datetime(2026, 2, 16, 12, 30, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING MEMORIAL DAY 3:30 PM WITH NAME: BUGS BUNNY:")
    fake_now = datetime(2026, 5, 25, 15, 30, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING JUNETEENTH 4:30 PM WITH NAME: BUGS BUNNY:")
    fake_now = datetime(2026, 6, 19, 16, 30, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING INDEPENDANCE DAY 7:30 PM WITH NAME: BUGS BUNNY:")
    fake_now = datetime(2026, 7, 4, 19, 30, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING LABOR DAY 10:30 PM WITH NAME: BUGS BUNNY:")
    fake_now = datetime(2026, 9, 7, 22, 30, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING COLUMBUS/INDIGENOUS PEOPLES DAY 11:00 PM WITH NAME: BUGS BUNNY:")
    fake_now = datetime(2026, 10, 12, 23, 0, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING VETERANS DAY 3:00 PM WITH NAME: BUGS BUNNY:")
    fake_now = datetime(2025, 11, 11, 15, 0, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING THANKSGIVING DAY 3:00 PM WITH NAME: BUGS BUNNY:")
    fake_now = datetime(2025, 11, 27, 15, 0, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print(f"\nTESTING CHRISTMAS MORNING AT 8:30 AM WITH NAME: BUGS BUNNY:")
    fake_now = datetime(2025, 12, 25, 8, 30, 0)
    with patch("greeting.datetime") as mock_datetime:
        # Make datetime.now() return our fake time
        mock_datetime.now.return_value = fake_now
        # Let datetime.strftime still behave normally
        mock_datetime.strftime = datetime.strftime
        print(build_greeting(name))

    print("")

if __name__ == "__main__":
    main()
