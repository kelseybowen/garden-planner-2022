from datetime import datetime, timedelta


def today_int():
    """Returns today's date as an integer"""
    today = datetime.now().timetuple().tm_yday
    return today


def date_to_int(mm_dd_yyyy: str):
    """Given any date, returns date as integer"""
    split_str = mm_dd_yyyy.split("/")
    year = int(split_str[2])
    month = int(split_str[0])
    day = int(split_str[1])
    date_as_int = datetime(year=year, month=month, day=day).strftime("%j")
    return date_as_int


def decode_date(date_as_int: int):
    """Takes in a date_as_int, returns month/day/year"""
    conversion = str(datetime(2022, 1, 1) + timedelta(date_as_int - 1))
    date_format1 = conversion.split(" ")
    date_format = date_format1[0].split("-")
    print(f"{date_format[1]}" + "/" + f"{date_format[2]}" + "/" + f"{date_format[0]}")