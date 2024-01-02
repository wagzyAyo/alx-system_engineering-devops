#!/usr/bin/python3
"""This module request data from
jsonplaceholder"""
import json
import requests
import sys


if __name__ == '__main__':
    end_point = "https://jsonplaceholder.typicode.com/"
    id = sys.argv[1]
    response = requests.get('{}users/{}'
                            .format(end_point, id)).json()
    name = response["name"]
    username = response['username']

    todos = requests.get('{}todos?userId={}'.
                         format(end_point, id)).json()
    new_list = []
    for todo in todos:
        dict = {'task': todo['title'], 'completed': todo['completed'],
                'username': username}
        new_list.append(dict)

    filename = '{}.json'.format(id)
    task = {str(id): new_list}
    with open(file=filename, mode='w') as file:
        json.dump(task, file)
