#!/usr/bin/python3
"""
Exercise 0:
Interacts with the APIs
at https://jsonplaceholder.typicode.com/
and gets info about the users'
to-do lists and which tasks have they completed.

Head over to https://jsonplaceholder.typicode.com/todos/
and https://jsonplaceholder.typicode.com/users
to understand how the JSON data is recieved by this program!
"""
import requests

if __name__ == "__main__":
    from sys import argv

    EMPLOYEE_ID = int(argv[1])

    ROOT_URL = "https://jsonplaceholder.typicode.com/"

    TODOS = requests.get(f'{ROOT_URL}todos/').json()
    EMPLOYEE_NAMES = requests.get(f'{ROOT_URL}users/').json()

    EMPLOYEE_NAME = EMPLOYEE_NAMES[EMPLOYEE_ID - 1]['name']

    EMPLOYEE_TODOS = tuple(
        task
        for task in TODOS
        if task['userId'] == EMPLOYEE_ID
    )