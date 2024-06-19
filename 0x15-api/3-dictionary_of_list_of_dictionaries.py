#!/usr/bin/python3
""" python to fetch Rest API for todo lists of employees """
import json
import requests
import sys

if __name__ == "__main__":
    """ Request user data from the commandline"""
    url = "https://jsonplaceholder.typicode.com/users/"

    resp = requests.get(url)
    users = resp.json()

    users_dict = {}
    for user in users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        url = url + '/todos/'
        resp = requests.get(url)

        tasks = resp.json()
        users_dict[USER_ID] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME})
    with open('todo_all_employee.json', 'w') as f:
        json.dump(users_dict, f)