#!/usr/bin/python3
"""
Model to export to json
"""

import json
from sys import argv
import requests

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"

    user_req = requests.get(f"{URL}users")
    user_data = user_req.json()

    todos = requests.get(f"{URL}todos")
    todos_data = todos.json()

    user_json = {}

    for user in user_data:
        list_all = []
        for todo in todos_data:
            if todo['userId'] == user['id']:
                list_all.append({"username": user['username'],
                                 "task": todo['title'],
                                 "completed": todo['completed']})

        user_json[str(user['id'])] = list_all

    with open(f"todo_all_employees.json", 'w') as file:
        json.dump(user_json, file)
