#!/usr/bin/python3
"""
Model to export to CSV
"""

import requests
import csv
from sys import argv

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    user_id = int(argv[1])

    user_req = requests.get(f"{URL}/users/{user_id}")
    data = user_req.json()
    user_name = data.get("username")

    todos = requests.get(f"{URL}/todos/")
    todos_data = todos.json()

    completed_todos = []
    total_todos = 0
    for todo in todos_data:
        if todo.get("userId") == user_id:
            completed_todos.append(todo)


# Export tasks to CSV
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)

    for todo in completed_todos:
        csv_writer.writerow([f'{user_id}',
                             f'{user_name}',
                             f'{todo["completed"]}',
                             f'{todo["title"]}'])
# Write csv data
        print(f"{csv_filename}")
