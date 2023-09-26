#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys
import csv


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employeeId>")
        sys.exit(1)

    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done_tasks = []

    for task in tasks:
        user_id = employeeId
        username = employeeName
        task_completed_status = task.get('completed')
        task_title = task.get('title')
        done_tasks.append((
            user_id,
            username,
            task_completed_status,
            task_title
        ))

    csv_filename = "{}.csv".format(employeeId)
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        ])

        writer.writerows(done_tasks)

    print("Data exported to {}.".format(csv_filename))
