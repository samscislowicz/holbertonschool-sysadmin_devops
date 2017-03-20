#!/usr/bin/python3
"""

"""
import requests
import sys


def get_data(userid):
    url = "https://jsonplaceholder.typicode.com"
    usr_id = sys.argv[1]
    user = requests.get(url + '/users/' + usr_id).json().get("name")
    todo = requests.get(url + '/todos?userId=' + usr_id).json()

    done_tasks = []
    total = 0
    done = 0

    for task in todo:
        if (task.get("userId") == int(usr_id)):
            total += 1
            if tasks.get('completed') is True:
                done += 1
                done_tasks.append(task.get("title"))

    print("Employee {} is done with tasks ({:d}/{:d}):"
          .format(user, done, total))

    for task in done_tasks:
        print("\t{}".format(task))

if __name__ == "__main__":
    usr_id = sys.argv[1]
    if len(sys.argv) > 1:
        get_data(usr_id)
