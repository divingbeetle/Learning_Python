"""

*** EX 16.2 ***
    Use the datetime module to write a program that gets
    the current date and prints the day of the week

    Write a program that takes a birthday as input and
    prints the user's age and the number of days, hours, minutes and seconds
    until their next birthday

    For two people born on different days,
    there is a day when one is twice as old as the other
    That's their Double Day.
    Write a program that takes two birth dates and computes their Double day

    For a challenge, write the more general version that computes the day
    when one person is n times older than the other
"""

from datetime import timedelta, datetime


def get_age(birthday):
    age = datetime.today().year - birthday.year + 1
    return age


def get_date_input():
    year_input = int(input("Year: "))
    month_input = int(input("Month: "))
    day_input = int(input("Day: "))
    res_date = datetime(year_input, month_input, day_input)
    return res_date


def til_birthday(birthday):
    this_birthday = birthday.replace(year=datetime.today().year)
    diff = this_birthday - datetime.today()

    if diff > timedelta(days=0):
        print("\nIt takes...")
        print("{0} Days, {1} Hours, {2} Minutes, {3} Seconds".format(*split_timedelta(diff)))
        print("until your birthday")

    elif diff > -timedelta(days=1):
        print("\nThis is your birthday")
        print("Happy birthday!")

    else:
        print("\nIt takes...")
        print("{0} Days, {1} Hours, {2} Minutes, {3} Seconds".format(*split_timedelta(diff + timedelta(days=365))))
        print("til your birthday\n")


def split_timedelta(td):
    res = str(td).split()[2].split(":")
    return td.days, res[0], res[1], res[2]


def get_nday(day1, day2, n):
    if day2 > day1:
        diff = day2 - day1
        return str(day2 + diff * n).split()[0], 1
    else:
        diff = day1 - day2
        return str(day1 + diff * n).split()[0], 2


def main():
    print("Welcome, please type your name")
    user_name = input("Username: ", )

    user_input = None

    print("""\n--Menu----------------------------

1. Get Today's Date
2. Calculate My age
3. Time Left Until Next Birthday
4. Calculate 'N-Day' of two people
0. Exit
----------------------------------\n""")
    while user_input != 0:
        user_input = int(input("Please Select a Menu: ", ))
        print()

        if user_input == 1:
            print("Today's date is..")
            print("{0}, {1}".format(datetime.today().date(), datetime.today().date().strftime("%A")))

        if user_input == 2:
            print("Please type your birthday")
            user_birthday = get_date_input()
            user_age = get_age(user_birthday)
            print(f"\nCurrent age of {user_name} is {user_age}\n")

        if user_input == 3:
            print("Please type your birthday")
            user_birthday = get_date_input()
            til_birthday(user_birthday)

        if user_input == 4:
            print("Please type person1's birthday")
            user1_birthday = get_date_input()
            print("\nPlease type person2's birthday")
            user2_birthday = get_date_input()
            N = int(input("\nN: ", ))
            print("\nIn {0}, person{1} will be {2} times older than other!".format(*get_nday(user1_birthday, user2_birthday, N), N))



if __name__ == "__main__":
    main()