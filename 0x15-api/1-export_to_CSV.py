#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
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

    total_tasks = 0

    # List to store CSV rows
    csv_rows = []

    for task in employee_data:
        if task['completed']:
            total_tasks += 1
            csv_rows.append([employee_id, employee_name, 'True', task['title']])
        else:
            csv_rows.append([employee_id, employee_name, 'False', task['title']])

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, total_tasks, len(employee_data)))

    for task in employee_data:
        if task['completed']:
            print("\t" + task['title'])

    # Export to CSV file
    csv_file_name = '{}.csv'.format(employee_id)
    with open(csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(csv_rows)

    print("Data exported to {}".format(csv_file_name))
