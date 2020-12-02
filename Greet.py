
def get_part_of_day(hour):
    return (
        "morning" if 5 <= hour <= 11
        else
        "afternoon" if 12 <= hour <= 17
        else
        "evening" if 18 <= hour <= 22
        else
        "night"
    )

#If you want to use current hour:
from datetime import datetime
h = datetime.now().hour
t=datetime.now().strftime("%I:%M %p")
d=datetime.now().strftime("%Y-%m-%d")
x=f'Today is {d}'
t=f"time is {t}"
d=f'have a good {get_part_of_day(h)}!\n'