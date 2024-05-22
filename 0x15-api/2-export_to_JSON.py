#!/usr/bin/python3
"""Export to JSON

This script exports user tasks from the JSONPlaceholder API to a JSON file.
It takes one argument, the user ID, and creates a JSON file named
<USER_ID>.json containing the tasks of that user in a nested dictionary
format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2 and argv[1].isdigit():
        USER_ID = argv[1]
        filename = "{}.json".format(USER_ID)
        url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(USER_ID)
        user = requests.get(
                "https://jsonplaceholder.typicode.com/user/{}"
                .format(USER_ID)).json()
        tasks = requests.get(url).json()

        data = {USER_ID: [{"task": task.get('title'),
                           "completed": task.get('completed'),
                           "username":
                           user.get('username')} for task in tasks]}

        with open(filename, mode='w') as file:
            json.dump(data, file)
