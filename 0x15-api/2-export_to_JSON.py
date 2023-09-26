#!/usr/bin/python3

"""Fetching data from an API and exporting it in JSON format"""
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

    # Create a list to store the tasks
    tasks = []

    # Extract and format task data
    for task in todo_data:
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        }
        tasks.append(task_data)

    # Create a dictionary for the JSON format
    user_data = {
        str(employee_id): tasks
    }

    # Write the data to a JSON file
    with open(f'{employee_id}.json', 'w') as json_file:
        json.dump(user_data, json_file, indent=4)

    print(f"Data exported to {employee_id}.json")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Invalid employee ID. Please provide an integer.")
