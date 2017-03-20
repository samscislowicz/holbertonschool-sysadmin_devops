#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    usr_id = sys.argv[1]
    user = requests.get(url + '/users/' + usr_id).json().get("name")
    todo = requests.get(url + '/todos?userId=' + usr_id).json()

    with open('{}.csv'.format(usr_id), 'w+') as f:
        writer = csv.writer(f, delimiter=' ',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for tasks in todo:
            writer.writerow([usr_id, user, task.get("completed"),
                             task.get("title")])
