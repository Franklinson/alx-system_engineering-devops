#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
"""

import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <employeeId>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    employee_url = f"{base_url}/{employee_id}"

    # Get employee information
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data.get('name')

    # Get employee's tasks
    tasks_url = f"{employee_url}/todos"
    response = requests.get(tasks_url)
    tasks = response.json()

    # Count completed tasks and collect them
    completed_tasks = [task for task in tasks if task.get('completed')]
    num_completed = len(completed_tasks)

    # Print employee's completed tasks
    print(
            f"Employee {employee_name} is done with tasks"
            f"({num_completed}/{len(tasks)}):")
    for task in completed_tasks:
        print(f"\t{task.get('title')}")


if __name__ == '__main__':
    main()
