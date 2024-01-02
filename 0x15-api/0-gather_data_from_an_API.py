#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    session = requests.Session()

    employee_id = argv[1]
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)

    employee_response = session.get(todos_url)
    user_response = session.get(user_url)

    employee_data = employee_response.json()
    employee_name = user_response.json().get('name')

    total_tasks = sum(1 for task in employee_data if task['completed'])

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, total_tasks, len(employee_data)))

    for task in employee_data:
        if task['completed']:
            print("\t" + task['title'])
