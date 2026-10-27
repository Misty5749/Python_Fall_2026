"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

import datetime


def header():
    file = open("bug_log.txt", "a")
    file.write("--- Bug fix tickets ---\n")
    file.write(f"{datetime.datetime.now()}\n")
    file.close()


def main():
    file_name = input("Please input the file name: ")
    priority = input("Please input the priority (low, medium, high): ")
    while True:
        bugs = input("Please input what bugs are happening and type done to end: ")
        bugs_list = []
        if bugs == "done":
            return bugs_list
        else:
            bugs_list.append(bugs)
            bug_ticket = {
                "timestamp": datetime.datetime.now(),
                "file_name": file_name,
                "description": bugs,
                "priority": priority,
            }
        with open("bug_log.txt", "a") as file:
            file.write(f"{bug_ticket}\n")
            file.write("-------------------------------")


header()
main()
