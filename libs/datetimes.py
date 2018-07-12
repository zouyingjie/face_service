# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

import time
from datetime import datetime as py_time
from datetime import timedelta

from dateutil.rrule import rrule, MONTHLY
from django.utils.timezone import is_naive, get_default_timezone, now, \
    make_naive, is_aware


DATE_FORMAT = "%Y-%m-%d"
DATE_FORMAT_V2 = "%Y/%m/%d"
TIME_FORMAT = "%H:%M:%S"
STRATEGY_TIME_FORMAT = "%H:%M"
DATETIME_FORMAT = "%sT%s" % (DATE_FORMAT, TIME_FORMAT)
DATE_AND_HOUR_FORMAT = "%sT%s" % (DATE_FORMAT, STRATEGY_TIME_FORMAT)
USE_MICROSECONDS = True


def time_to_str(time, format=STRATEGY_TIME_FORMAT):
    return time.strftime(format)


def date_to_str(date, format=DATE_FORMAT):
    return date.strftime(format)


def datetime_to_str(datetime, format=DATETIME_FORMAT):
    if is_aware(datetime):
        datetime = to_naive_datetime(datetime)

    return datetime.strftime(format.encode('utf-8')).decode('utf-8')


def datetime_delta(datetime, **kwargs):
    delta = timedelta(**kwargs)
    return datetime + delta


def str_to_datetime(str, format=DATETIME_FORMAT):
    if isinstance(str, py_time):
        if is_naive(str):
            return to_aware_datetime(str)
        else:
            return str
    if format == DATE_AND_HOUR_FORMAT:
        if len(str.split(":")) == 2:
            str += ":00"
        format = DATETIME_FORMAT
    return to_aware_datetime(py_time.strptime(str, format))


def to_aware_datetime(value):
    if is_aware(value):
        return value
    time_zone = get_default_timezone()
    # http://stackoverflow.com/questions/21465528/resolving-ambiguoustimeerror-from-djangos-make-aware
    return time_zone.localize(value, is_dst=False)


def to_naive_datetime(value):
    if is_naive(value):
        return value
    time_zone = get_default_timezone()
    return make_naive(value, time_zone)


def datetime_now():
    return now()


def dates_during(from_date, to_date, weekdays=None):
    if weekdays is None:
        weekdays = range(1, 8)
    if not weekdays:
        weekdays = []

    dates = []
    delta_day = (to_date - from_date).days
    for delta in range(0, delta_day + 1):
        date = from_date + timedelta(days=delta)
        if date.weekday() + 1 in weekdays:
            dates.append(date)
    return dates


def get_weekday(datetime):
    if is_aware(datetime):
        datetime = to_naive_datetime(datetime)
    days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    return days[datetime.weekday()]


def datetime_to_timestamp(datetime, use_microseconds=USE_MICROSECONDS):
    if is_aware(datetime):
        datetime = to_naive_datetime(datetime)
    timetuple = datetime.timetuple()
    seconds = time.mktime(timetuple)
    if use_microseconds:
        return seconds * 1000
    else:
        return seconds


def timestamp_to_datetime(timestamp, use_microseconds=USE_MICROSECONDS):
    if use_microseconds:
        timestamp = float(timestamp) / 1000
    else:
        timestamp = float(timestamp)

    datetime = py_time.fromtimestamp(timestamp)
    return datetime


def str_to_time(input_str):
    from datetime import time
    hour, minute = input_str.split(":")
    return time(int(hour), int(minute))


def time_delta(from_time, seconds=3600):
    from datetime import date, datetime, timedelta
    dt = datetime.combine(date.today(), from_time) + timedelta(seconds=seconds)
    return dt.time()


def str_to_date(input_str):
    return str_to_datetime(input_str, DATE_FORMAT).date()


def str_to_birthday(input_str):
    if not input_str:
        return None
    return str_to_datetime(input_str, DATE_FORMAT).date()


def get_week_from_to(datetime):
    return datetime_delta(
        datetime,
        days=-datetime.weekday()
    ), datetime_delta(datetime, days=6 - datetime.weekday())


def get_month_from_to(input):
    month_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1]
    year = input.year
    month = input.month
    month_to = month_list[month - 1]
    if month_to == 1:
        to_year = year + 1
    else:
        to_year = year
    return py_time(year=year, month=month, day=1), py_time(year=to_year,
                                                           month=month_to,
                                                           day=1)


def get_datetime_fragments(from_date, to_date, weekday, start, end, is_cross=False):
    datetimes = []
    delta_day = (to_date - from_date).days
    for delta in range(0, delta_day + 1):
        date = from_date + timedelta(days=delta)
        if date.weekday() + 1 == weekday:
            datetime_start = to_aware_datetime(
                py_time.combine(date.date(), start))
            if is_cross:
                datetime_end = to_aware_datetime(py_time.combine(datetime_delta(date, days=1).date(), end))
            else:
                datetime_end = to_aware_datetime(py_time.combine(date.date(), end))
            datetimes.append([datetime_start, datetime_end])
    return datetimes


def datetime_in_start_end(datetime, start, end):
    compare_date = to_naive_datetime(datetime).date()
    start_date = to_naive_datetime(start).date()
    end_date = to_naive_datetime(datetime_delta(end, days=1)).date()

    if compare_date >= start_date and compare_date < end_date:
        return True
    return False


def get_months(from_date, to_date):
    dates = [dt for dt in rrule(MONTHLY, dtstart=to_naive_datetime(from_date),
                                until=to_naive_datetime(to_date))]
    return dates


def get_latest_from_to(start, end, days=1):
    if start and end:
        start = str_to_datetime(start, format=DATE_FORMAT)
        end = str_to_datetime(end, format=DATE_FORMAT)
        end = datetime_delta(end, days=1)
    else:
        today = str_to_datetime(
            date_to_str(to_naive_datetime(datetime_now()).date()),
            format=DATE_FORMAT)
        end = datetime_delta(today, days=1)
        start = datetime_delta(end, days=-days)

    return start, end


def get_detla_day(input_date, days=1):
    try:
        if is_aware(input_date):
            input_date = to_naive_datetime(input_date)
        next_day = datetime_delta(input_date.replace(
            hour=0, minute=0, second=0, microsecond=0), days=days)
        return to_aware_datetime(next_day)
    except:
        return datetime_delta(datetime_now().replace(
            hour=0, minute=0, second=0, microsecond=0), days=days)


def get_before_day(input_date, days=1):
    return get_detla_day(input_date, days=-days)


def get_this_day(input_date):
    return get_detla_day(input_date, days=0)


def get_after_day(input_date, days=1):
    return get_detla_day(input_date, days=days)


def get_next_day(input_date):
    return get_detla_day(input_date, days=1)


def datetime_to_string(datetime):
        return datetime_to_str(
            datetime,
            u"%Y年%m月%d日 {0} %H:%M".format(get_weekday(datetime))
        )


def date_to_string(datetime):
    return datetime_to_str(
        datetime,
        u"%Y年%m月%d日"
    )
