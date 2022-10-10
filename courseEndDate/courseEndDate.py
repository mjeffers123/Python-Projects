from datetime import datetime, timedelta


def getCourseEndDate():
    endDateStr = input("Enter Course End Date (MM/DD/YYYY): ")
    while True:
        try:
            endDate = datetime.strptime(endDateStr, "%m/%d/%Y")
            break
        except:
            print("Invalid date format. Try again.")
            continue
    return datetime(endDate.year, endDate.month, endDate.day)


def main():
    print()
    print("Days to End of Course Calculator")
    print()

    userName = input("Enter Name: ")
    courseEndDate = getCourseEndDate()

    endDate = courseEndDate
    currentDate = datetime.today()
    currentDateStr = currentDate.strftime("%A, %B %d, %Y")
    daysLeft = (currentDate - endDate).days * -1
    weeksLeft = str(round(daysLeft / 7))
    daysRemainder = str(daysLeft % 7)

    print("Current Date: " + currentDateStr)
    print(f"The course end date is in {daysLeft} days")
    print(
        f"The course has {weeksLeft} Weeks and {daysRemainder} Days left")


main()
