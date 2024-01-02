#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Get user info
    user_url = "{}/users/{}".format(base_url, employee_id)
    response_user = requests.get(user_url)
    user_data = response_user.json()

    # Get user's TODO list
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    response_todos = requests.get(todos_url)
    todos_data = response_todos.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos_data if task['completed']]

    # Display information
    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], len(completed_tasks), len(todos_data)))

    for task in completed_tasks:
        print("\t {}".format(task['title']))

