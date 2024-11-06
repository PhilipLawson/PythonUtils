year_array = (0,3,3,6,1,4,6,2,5,0,3,5)
days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")


def get_day_int(date):
    try:
        user_day = int(date.split("/")[0]) 
        user_month = int((date.split("/")[1]))
        user_year = int((date.split("/")[2]))
        y = [ 0, 3, 2, 5, 0, 3,
            5, 1, 4, 6, 2, 4 ]
        user_year -= user_month < 3
        return (( user_year + int(user_year / 4) - int(user_year / 100)
                + int(user_year / 400) + y[user_month - 1] + user_day) % 7)
    except IndexError:
        print(f"Please make sure you enter the full date in dd/mm/yyyy format")


def main():
    user_day = str(input(f"Please enter a date [dd/mm/yyyy]: "))
    day = days_of_the_week[get_day_int(user_day)]
    print(f"{day}")


if __name__ == "__main__":
    main()