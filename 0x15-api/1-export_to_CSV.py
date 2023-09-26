#!/usr/bin/python3

"""Fetching data from an API and exporting to CSV"""
import requests
import csv
import sys


def get_employee_todo_progress(employee_id):
    # Define the base URL of the REST API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Make a GET request to fetch employee information
    employee_response = requests.get(
        base_url + f'users/{employee_id}')
    employee_data = employee_response.json()
    user_id = employee_data['id']
    username = employee_data['username']

    # Make a GET request to fetch the employee's TODO list
    todo_response = requests.get(
        base_url + f'todos?userId={employee_id}')
    todo_data = todo_response.json()

    # Prepare the data for CSV export
    csv_data = []
    for task in todo_data:
        task_completed_status = (
            "Completed" if task['completed'] else "Not Completed"
        )
        task_title = task['title']
        csv_data.append([user_id, username, task_completed_status, task_title])

    # Create and write to the CSV file
    csv_filename = f'{user_id}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        )
        csv_writer.writerows(csv_data)

    print(f"Data exported to {csv_filename}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Invalid employee ID. Please provide an integer.")
