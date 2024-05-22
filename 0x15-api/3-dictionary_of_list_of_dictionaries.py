#!/usr/bin/python3
"""Dictionary of list of dictionaries

This script exports tasks of all users from the JSONPlaceholder API to a JSON
file.It retrieves tasks for each user and stores them in a nested dictionary,
where the keys are user IDs and the values are lists of dictionaries containing
task details.The resulting JSON file is named todo_all_employees.json.
"""

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    data = {}
    for user in users:
        USER_ID = str(user.get("id"))
        username = user.get("username")
        tasks = requests.get(url, params={"userId": USER_ID}).json()
        data[USER_ID] = [{"username": username,
                          "task": task.get("title"),
                          "completed":
                          task.get("completed")} for task in tasks]
        with open("todo_all_employees.json", mode='w') as file:
            json.dump(data, file)
