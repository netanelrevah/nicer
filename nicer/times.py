from datetime import datetime, timedelta
import time

import pytz

from nicer.eqs import ComparableMixin

__author__ = 'netanelrevah'


def current_datetime():
    return datetime.now(pytz.UTC)


def seconds_from_datetime(value):
    return int(seconds_from_timedelta(value - datetime(1970, 1, 1, tzinfo=pytz.UTC)))


def microseconds_from_datetime(value):
    return value.microsecond


def seconds_from_timedelta(value):
    return .0 + value.days * 24 * 60 * 60 + value.seconds + value.microseconds / 1000000.


def hours_from_timedelta(value):
    return seconds_from_timedelta(value) / 60


def hours_delta(hours):
    if isinstance(hours, int):
        hours = timedelta(hours=hours)
    if not isinstance(hours, timedelta):
        raise TypeError("Not Supported Type!")
    return hours


def datetime_from_timestamp(value):
    return datetime.fromtimestamp(value, pytz.UTC)


def datetime_from_seconds_and_microseconds(seconds, microseconds):
    return datetime.fromtimestamp(seconds, pytz.UTC) + timedelta(microseconds=microseconds)


class Timestamp(ComparableMixin):
    def __init__(self, seconds, second_parts=0):
        self.seconds = seconds
        self.seconds_parts = second_parts

    @staticmethod
    def now(precision=9):
        return Timestamp.from_timestamp(time.time(), precision)

    @staticmethod
    def from_timestamp(timestamp, precision=9):
        return Timestamp(int(timestamp), int((timestamp % 1) * (10 ** precision)))

    @staticmethod
    def from_datetime(dt):
        return Timestamp(seconds_from_datetime(dt), microseconds_from_datetime(dt))

    def __lt__(self, other):
        return not (self >= other)

    def __le__(self, other):
        if isinstance(other, Timestamp):
            return ((self == other)
                    or (self.seconds < other.seconds)
                    or (self.seconds == other.seconds and self.seconds_parts > other.seconds_parts))
        raise TypeError()

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        if isinstance(other, Timestamp):
            return ((self == other)
                    or (self.seconds > other.seconds)
                    or (self.seconds == other.seconds and self.seconds_parts > other.seconds_parts))
        raise TypeError()

    def to_comparable(self):
        return self.seconds, self.seconds_parts
