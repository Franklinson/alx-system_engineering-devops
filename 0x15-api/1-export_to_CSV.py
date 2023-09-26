#!/usr/bin/python3

"""Fetching data from an API and exporting it to CSV"""

import requests
import sys
import csv


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

        # Create and write CSV file
        csv_file_name = f"{employee_name}.csv"
        with open(csv_file_name, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"
            ])

            # Write task data to CSV
            for task in todos:
                csv_writer.writerow([
                    task['userId'],
                    employee_name,
                    task['completed'],
                    task['title']
                ])

        print(f"Data exported to {csv_file_name}")

    except requests.exceptions.HTTPError as err:
        print(f"Error fetching data from the API: {err}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
