#!/usr/bin/python3
"""
Export tasks of all employees to a JSON file.

This script retrieves task data for all employees from a dummy API
(https://jsonplaceholder.typicode.com) and exports it to a JSON file
(todo_all_employees.json) in the specified format.

Requirements:
    - The requests module must be installed 
    (you can install it using 'pip install requests').
    - The script should be run with Python 3.

Usage:
    python3 3-dictionary_of_list_of_dictionaries.py
"""


# Fetch data for all users
users_url = 'https://jsonplaceholder.typicode.com/users'
users_response = session.get(users_url)
users_data = users_response.json()

# Dictionary to store all tasks for each user
all_tasks = {}

for user in users_data:
    employee_id = user['id']
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        employee_id
    )

    employee_response = session.get(todos_url)
    employee_data = employee_response.json()

    # List to store JSON objects for each user
    json_objects = []

    for task in employee_data:
        json_objects.append({
            "username": user['username'],
            "task": task['title'],
            "completed": task['completed']
        })

    # Add the list of tasks to the dictionary
    all_tasks[str(employee_id)] = json_objects

# Export to JSON file
json_file_name = 'todo_all_employees.json'
with open(json_file_name, 'w') as jsonfile:
    json.dump(all_tasks, jsonfile)

print("Data exported to {}".format(json_file_name))
