#!/usr/bin/python3

"""Fetching data from an API and exporting to JSON"""

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

        # Filter completed tasks and count them
        completed_tasks = []
        for task in todos:
            if task['completed']:
                task_data = {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": todos[0]['username']
                }
                completed_tasks.append(task_data)

        # Create a dictionary with the required format
        user_data = {
            str(employee_id): completed_tasks
        }

        # Export data to a JSON file
        output_filename = f'{employee_id}.json'
        with open(output_filename, 'w') as json_file:
            json.dump(user_data, json_file, indent=4)

        print(f"Data exported to {output_filename}")

    except requests.exceptions.HTTPError as err:
        print(f"Error fetching data from the API: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
