#!/usr/bin/python3
"""Export to CSV

This script exports user tasks from the JSONPlaceholder API to a CSV file.
It takes one argument, the user ID, and creates a CSV file named <USER_ID>.csv
containing the tasks of that user. The CSV file has the following format:
USER_ID, USERNAME, COMPLETED, TITLE
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2 and argv[1].isdigit():
        USER_ID = argv[1]
        filename = "{}.csv".format(USER_ID)
        url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(USER_ID)
        user = requests.get(
                "https://jsonplaceholder.typicode.com/users/{}"
                .format(USER_ID)).json()
        tasks = requests.get(url).json()

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in tasks:
                writer.writerow([USER_ID, user.get('username'),
                                task.get('completed'), task.get('title')])
