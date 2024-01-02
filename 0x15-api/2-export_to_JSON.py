#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports it to JSON.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    session = requests.Session()

    employee_id = argv[1]
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    .format(employee_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'
    .format(employee_id)

    employee_response = session.get(todos_url)
    user_response = session.get(user_url)

    employee_data = employee_response.json()
    employee_name = user_response.json().get('name')

    total_tasks = 0

    # List to store JSON objects
    json_objects = []

    for task in employee_data:
        total_tasks += 1
        json_objects.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        })

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, total_tasks, len(employee_data)))

    for task in employee_data:
        if task['completed']:
            print("\t" + task['title'])

    # Export to JSON file
    json_file_name = '{}.json'.format(employee_id)
    with open(json_file_name, 'w') as jsonfile:
        json.dump({employee_id: json_objects}, jsonfile)

    print("Data exported to {}".format(json_file_name))
