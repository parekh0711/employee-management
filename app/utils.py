import string
import random
import os
from collections import defaultdict
import datetime

day_dict = defaultdict(lambda: "th")
day_dict = {1: "st", 2: "nd", 3: "rd", 11: "th", 12: "th", 13: "th"}
month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}


def cleanup(files):
    for file in files:
        os.remove(file)


def generate_string(length=5):
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )


def cleanup(files):
    for file in files:
        os.remove(file)


def convert_date(date):
    if date == "-":
        return date
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    result = ""
    result += str(date.day)
    # if date.month not in [11, 12, 13]:
    #     result += day_dict(date.month % 10)
    # else:
    #     result += day_dict(date.month)
    result += " " + month_dict[date.month] + ", " + str(date.year)
    print(result)
    return result
