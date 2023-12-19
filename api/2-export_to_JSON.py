#!/usr/bin/python3
"""
Model to export to json
"""

import json
from sys import argv
import requests

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
            total_todos += 1
            completed_todos.append(todo)

    user_dict = []

    for todo in completed_todos:
        user_dict.append({"task": todo['title'],
                          "completed": todo['completed'],
                          "username": user_name})

    json_object = {f"{user_id}": user_dict}

    with open(f"{user_id}.json", 'w') as file:
        json.dump(json_object, file)
