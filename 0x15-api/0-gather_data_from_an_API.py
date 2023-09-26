#!/usr/bin/python3

"""Fetching data from an API"""
import requests
import sys


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
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todo_data)

    # Display the employee's TODO list progress
    print(
        f"Employee {employee_name} is done with tasks"
        f"({num_completed_tasks}/{total_num_tasks}): ")

    # Display the titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Invalid employee ID. Please provide an integer.")
