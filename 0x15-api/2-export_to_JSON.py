#!/usr/bin/python3
"""Export data to json format """

import csv
import json
import requests
from sys import argv

emp_info = 'https://jsonplaceholder.typicode.com/users/'
all_todos = 'https://jsonplaceholder.typicode.com/todos'
if __name__ == "__main__":
    emp_id = argv[1]
    get_emp_info = json.loads(requests.get(emp_info + emp_id).text)
    get_all_todos = json.loads(requests.get(all_todos).text)
    todos_done_list = []
    name = None

    to_js = dict()
    todos = []
    for i in get_all_todos:
        if i['userId'] == int(emp_id):
            this_info = {"task": i['title'], "completed": i['completed'],
                         "username": get_emp_info['username']}
            todos.append(this_info)
    to_js[emp_id] = todos
    with open("{}.json".format(emp_id), "w", encoding="utf8") as f:
        f.write(json.dumps(to_js))
