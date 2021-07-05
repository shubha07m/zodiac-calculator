def dobprint():
    d = int(input("Please enter your date of your birth in DD format:\n"))
    while d > 31:
        d = int(input("Please enter the date in range:\n"))

        if d < 31:
            break

    m = int(input("Please enter your month of your birth in MM format:\n"))
    while m > 12:
        m = int(input("Please enter the month in range:\n"))
        if m < 12:
            break

    month_list = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
                  9: 'September', 10: 'October',
                  11: 'November', 12: 'December'}

    month = month_list[m]

    y = int(input("Please enter your year of your birth in YYYY:\n"))
    while y > 2021:
        y = int(input("Please enter the year in range:\n"))
        if y < 2021:
            break

    print("So you born on " + str(d) + "th  " + month + "  " + str(y) + "")
    return m, d


def zodiac():
    m, d = dobprint()

    if ((m == 3) and (21 <= d <= 31)) or ((m == 4) and (19 >= d >= 1)):
        z = "Aries"
    elif ((m == 4) and (20 <= d <= 30)) or ((m == 5) and (20 >= d >= 1)):
        z = "Tauras"
    elif ((m == 5) and (21 <= d <= 31)) or ((m == 6) and (20 >= d >= 1)):
        z = "Gemini"
    elif ((m == 6) and (21 <= d <= 30)) or ((m == 7) and (22 >= d >= 1)):
        z = "Cancer"
    elif ((m == 7) and (23 <= d <= 31)) or ((m == 8) and (22 >= d >= 1)):
        z = "Leo"
    elif ((m == 8) and (23 <= d <= 31)) or ((m == 9) and (22 >= d >= 1)):
        z = "Virgo"
    elif ((m == 9) and (23 <= d <= 30)) or ((m == 10) and (22 >= d >= 1)):
        z = "Libra"
    elif ((m == 10) and (23 <= d <= 31)) or ((m == 11) and (21 >= d >= 1)):
        z = "Scorpio"
    elif ((m == 11) and (23 <= d <= 30)) or ((m == 12) and (21 >= d >= 1)):
        z = "Sagittarius"
    elif ((m == 12) and (22 <= d <= 31)) or ((m == 1) and (19 >= d >= 1)):
        z = "Capricorn"
    elif ((m == 1) and (20 <= d <= 31)) or ((m == 2) and (18 >= d >= 1)):
        z = "Aquarius"
    else:
        z = "Pisces"
    print("your zodiac sign is " + z + " ")


zodiac()
