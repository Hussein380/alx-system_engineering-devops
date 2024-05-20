#!/usr/bin/python3
"""
    Gather employee data from API
"""
import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        """ uses regular expression to see if first arg is digit """
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            """ Fecth employee data """
            req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            """ Fetch TODO list Data """
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            """ Extract Employee Name """
            emp_name = req.get('name')
            """ Filter tasks for Employees """
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            """ filter completed tasks """
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            """ Print the Employees's Tasks progress """
            print(
                    'Employee {} is done with ({}/{}):'.format(
                        emp_name,
                        len(completed_tasks),
                        len(tasks)
                        )
                    )
            """ Print the completed tasks Tiltles """
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
