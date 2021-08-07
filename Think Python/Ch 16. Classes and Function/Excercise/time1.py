class Time:
    """Represents the time of day.

    attributes: hour, minute, second"""


def print_time(t):
    print(f"{t.hour:>02}:{t.minute:>02}:{t.second:>02}")


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    time.minute = int(time.minute)
    time.hour = int(time.hour)
    time.second = int(time.second)
    return time


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def add_times(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


def increment(t1, seconds):
    assert valid_time(t1)
    seconds += time_to_int(t1)
    return int_to_time(seconds)
