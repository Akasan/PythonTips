from datetime import datetime


def generate_timestamp(is_year=True, is_month=True, is_day=True,
                       is_hour=True, is_minute=True, is_second=True,
                       is_year_digit_4=True, is_padding=True,
                       is_separate_date_and_time=True,
                       separate_character="_"):
    """ This function generate timestamp.
        You can use this function result for making file name according to the timestamp
    Keyword Arguments:
        is_year {bool} -- whether contain year (default: True)
        is_month {bool} -- whether contain month (default: True)
        is_day {bool} -- whether contain day (default: True)
        is_hour {bool} -- whether contain hour (default: True)
        is_minute {bool} -- whether contain minute (default: True)
        is_second {bool} -- whether contain second (default: True)
        is_year_digit_4 {bool} -- whether the number of digits for year is 4 or not (default: True)
        is_padding {bool} -- whether padding each number (default: True)
        is_separate_date_and_time {bool} -- whether separate date and time (default: True)
        separate_character {str} -- character when separate date and time
    """
    now = datetime.now()
    timestamp = ""
    
    element = {
        "year" : str(now.year),
        "month": str(now.month),
        "day": str(now.day),
        "separate": separate_character if is_separate_date_and_time else "",
        "hour": str(now.hour),
        "minute": str(now.minute),
        "second":str(now.second)
    }
    
    element["year"] = (element["year"] if is_year_digit_4 else element["year"][2:]) if is_year else ""
    element["month"] = (element["month"].zfill(2) if is_padding else element["month"]) if is_month else ""
    element["day"] = (element["day"].zfill(2) if is_padding else element["day"]) if is_day else ""
    element["hour"] = (element["hour"].zfill(2) if is_padding else element["hour"]) if is_hour else ""
    element["minute"] = (element["minute"].zfill(2) if is_padding else element["minute"]) if is_minute else ""
    element["second"] = (element["second"].zfill(2) if is_padding else element["second"]) if is_second else ""

    timestamp = "".join(list(element.values()))
    return timestamp
