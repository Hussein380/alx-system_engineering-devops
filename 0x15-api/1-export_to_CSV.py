#!/usr/bin/python3
""" Export api to csv """
import csv
import requests
import sys

if __name__ == "__main__":
    """ Extract user id from commandline """
    user = sys.argv[1]
    """ Request user data from the commandline"""
    url_user = "https://jsonplaceholder.typicode.com/users/" + user
    res = requests.get(url_user)

    """ Extract username from API response """
    user_name = res.json().get("username")
    """ Request user task from API response """
    task = url_user + '/todos'
    res = requests.get(task)
    tasks = res.json()

    """ open csv file and write to it """
    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
