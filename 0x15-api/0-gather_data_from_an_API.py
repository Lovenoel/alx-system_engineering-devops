#!/usr/bin/python3
"""
Python script that returns an employee's TODO list using a REST API.

This script fetches user data and their TODO list from the JSONPlaceholder API
and prints the number of completed tasks and their titles for a given employee.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress of an employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Get user info
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    if user_response.status_code != 200:
        print("Error fetching user data")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Get todo list for the user
    todoUs = requests.get(f'{base_url}/todos', params={'userId': employee_id})
    if todoUs.status_code != 200:
        print("Error fetching todos")
        return

    todos = todoUs.json()

    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo.get('completed')]
    number_of_done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
