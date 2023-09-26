#!/usr/binpython3

"""Fetching data from an API"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    # Define the API endpoint URL
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    try:
        # Send a GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()

        # Parse the JSON response
        todos = response.json()

        # Filter completed tasks and count them
        completed_tasks = [task for task in todos if task['completed']]
        num_completed_tasks = len(completed_tasks)

        # Calculate the total number of tasks
        total_tasks = len(todos)

        # Get the employee's name
        employee_name = todos[0]['userId']

        # Display the progress
        print(f"Employee {employee_name} is done with tasks "
              f"({num_completed_tasks}/{total_tasks}):")

        # Display the titles of completed tasks
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.HTTPError as err:
        print(f"Error fetching data from the API: {err}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
