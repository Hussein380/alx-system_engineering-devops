#!/usr/bin/python3
""" python to get data from an API and convert to json """
import csv
import json
import requests
import sys

if __name__ == "__main__":
    """ Extract user id from commandline """
    USER_ID = sys.argv[1]
    """ Request user data from the commandline"""
    url_to_user = "https://jsonplaceholder.typicode.com/users/" + USER_ID
    res = requests.get(url_to_user)

    """ Extract username from API response """
    USERNAME = res.json().get("username")
    """ Request user task from API response """
    url_to_task = url_to_user + '/todos'
    res = requests.get(url_to_task)
    tasks = res.json()

    """ dictionary to store data """
    dict_data = {USER_ID: []}

    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
            "username": USERNAME})
        with open('{}.json'.format(USER_ID), 'w') as f:
            json.dump(dict_data, f)
