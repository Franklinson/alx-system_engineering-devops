#!/usr/bin/python3

"""Fetching data from an API and exporting in JSON format"""
import requests
import sys
import json


def get_employee_todo_progress(employee_id):
    # Define the base URL of the REST API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Make a GET request to fetch employee information
    employee_response = requests.get(base_url + f'users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Make a GET request to fetch the employee's TODO list
    todo_response = requests.get(base_url + f'todos?userId={employee_id}')
    todo_data = todo_response.json()

    # Calculate the number of completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]

    # Return a dictionary representing the user's tasks
    return {
        "username": employee_name,
        "tasks": [
            {
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in completed_tasks
        ]
    }


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage: python script.py")
        sys.exit(1)

    # Create a dictionary to store tasks for all employees
    all_employee_tasks = {}

    try:
        # Fetch tasks for all users (employee IDs 1 to 10)
        for employee_id in range(1, 11):
            employee_tasks = get_employee_todo_progress(employee_id)
            all_employee_tasks[employee_id] = employee_tasks
    except ValueError:
        print("Invalid employee ID. Please provide an integer.")

    # Export the data in JSON format
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_employee_tasks, json_file, indent=4)

    print("Data exported to todo_all_employees.json")
