#!/usr/bin/python3
"""This module requests data from
jsonplaceholder"""
import json
import requests
import sys

if __name__ == '__main__':
    end_point = "https://jsonplaceholder.typicode.com/"
    task = {}

    users = requests.get('{}users'.format(end_point)).json()

    for user in users:
        id = user.get('id')
        name = user.get('name')
        username = user.get('username')

        todos = requests.get('{}todos?userId={}'.format(end_point, id)).json()
        new_list = []

        for todo in todos:
            task_dict = {
                'username': username,
                'task': todo['title'],
                'completed': todo['completed'],
            }
            new_list.append(task_dict)

        task[str(id)] = new_list

    filename = 'todo_all_employees.json'

    with open(filename, 'w') as file:
        json.dump(task, file)
