"""

*** EX 17.1 ***
    Change the attributes of Time to be a single integer
    representing seconds since midnight.

    Then modify the methods (and the function int_to_time)
    to work w/ new implementation

"""


class Time:
    """Represents the time of the day

    attributes: seconds(seconds since midnight)
    """
    def __init__(self, hour=0, minute=0, second=0):
        minutes = hour * 60 + minute
        self.seconds = minutes * 60 + second

    def __str__(self):
        minutes, second = divmod(self.seconds, 60)
        hour, minute = divmod(minutes, 60)
        return '%.2d:%.2d:%.2d' % (hour, minute, second)

    def __add__(self, other):
        sum = Time()
        if isinstance(other, Time):
            sum.seconds = self.seconds + other.seconds
        else:
            sum.seconds = self.seconds + other
        return sum

    def __radd__(self, other):
        return self.__add__(other)

    def is_after(self, other):
        return self.seconds > other.seconds


def main():
    start = Time(9, 45, 0)
    duration = Time(1, 35, 0)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == "__main__":
    main()
