#!/usr/bin/python3

"""Fetching data from an API and exporting it to JSON"""

import requests
import sys
import json


def get_employee_todo_progress(employee_id):
    # Define the API endpoint URL
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    try:
        # Send a GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()

        # Parse the JSON response
        todos = response.json()

        # Get the employee's name
        employee_name = todos[0]['userId']

        # Create a dictionary to store the tasks for this employee
        employee_tasks = {"username": employee_name, "tasks": []}

        # Populate the tasks list for this employee
        for task in todos:
            employee_tasks["tasks"].append({
                "task": task["title"],
                "completed": task["completed"]
            })

        return employee_tasks

    except requests.exceptions.HTTPError as err:
        print(f"Error fetching data from the API: {err}")
        return None


def export_to_json(data):
    if data is not None:
        with open("todo_all_employees.json", "a") as json_file:
            json.dump(data, json_file)
            json_file.write("\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Initialize an empty list to store all employee tasks
    all_employee_tasks = []

    # Loop through employee IDs (assuming you have a range of IDs)
    for employee_id in range(1, 11):  # Assuming IDs range from 1 to 10
        employee_tasks = get_employee_todo_progress(employee_id)
        if employee_tasks:
            all_employee_tasks.append(employee_tasks)

    # Export all employee tasks to JSON
    for employee_data in all_employee_tasks:
        export_to_json(employee_data)

    print("Data exported to todo_all_employees.json")
