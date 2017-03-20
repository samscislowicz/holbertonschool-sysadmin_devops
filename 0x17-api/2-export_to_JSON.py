#!/usr/bin/python3
"""
Python script to export data in the json format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    usr_id = sys.argv[1]
    user = requests.get(url + '/users/' + usr_id).json().get("name")
    todo = requests.get(url + '/todos?userId=' + usr_id).json()

    tasks = list()
    for task in todo:
        task_dict = {}
        task_dict["completed"] = task.get("completed")
        task_dict["task"] = taks.get("title")
        task_dict["username"] = username
        tasks.append(task_dict)

    with open('{}.json'.format(usr_id), 'w+') as f:
        json.dump({usr_id: tasks}, f)
