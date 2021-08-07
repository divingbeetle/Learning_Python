"""

*** EX 16.1 ***
    Write a d function called mul_time that takes a Time object and number and
    returns a new Time object that contains the product of the original Time and the number

    Then use mul_time to write a function that takes a Time object that
    represents the finishing time in a race, and
    a number that represents the distance, and
    returns a Time object that represents the average pace (time per mile)

"""

from time1 import *


def mul_time(t1, num):
    assert valid_time(t1)
    mul = time_to_int(t1) * num
    return int_to_time(mul)


def get_average_pace(fin_time, distance):
    return mul_time(fin_time, (1 / distance))


if __name__ == "__main__":
    test_time = Time()
    test_time.hour = 1
    test_time.minute = 30
    test_time.second = 10

    print_time(get_average_pace(test_time, 10))