# Project 2 - Jake Hemmelgarn

This script outputs the time, date, and days until the New Year 

I used the below sites as guides:

“Using Python Datetime to Work with Dates and Times.” Real Python, Real Python, 25 Sept. 2023, realpython.com/python-datetime/. 
Kaplarevic, Vladimir. “How to Get Current Date &amp; Time in Python {easy Options}.” Knowledge Base by phoenixNAP, 9 Aug. 2023, phoenixnap.com/kb/get-current-date-time-python. 

I ran this script in powershell using python project2.pys

```
import time
from datetime import date

time_now = time.strftime("%H:%M:%S")

print("The time is: ", time_now)

date_today = date.today()

print("Today's date is: ", date_today)

new_year = date(date_today.year + 1, 1, 1)

until_new_year = (new_year - date_today).days

print(f"There are {until_new_year} days until {new_year.year}")
```
