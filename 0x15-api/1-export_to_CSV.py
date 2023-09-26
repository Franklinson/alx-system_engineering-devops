#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

with open(f'{employeeId}.csv', 'w') as file:
    for task in tasks:
        employeeId = employeeId
        username = username
        completed = task.get('completed')
        title = task.get('title')
        file.write(f'"{employeeId}","{username}","{completed}","{title}"\n')
