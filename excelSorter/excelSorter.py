# super sorter by Matthew Jeffers

import csv

FILENAME = 'excelSorter\\to_do_list.csv'


def read_items():     # get list from file
    items = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            items.append(row)
        return items


def display_items(list):    # display list in standard text format
    for i in range(len(list)):
        chore = list[i]
        print(str(*chore))


def write_items(list):    # update file with sorted list
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(list)


def main():
    print()
    print("**To Do List!**")
    print()

    check = "n"

    while check.lower() == "n":
        list_items = sorted(read_items())     # sort list from read_items
        display_items(list_items)
        print()
        check = input("List sorted correctly? (y or n): ")
    write_items(list_items)
    print()
    print("List has been sorted and saved, bye!")
    print()


if __name__ == "__main__":
    main()
