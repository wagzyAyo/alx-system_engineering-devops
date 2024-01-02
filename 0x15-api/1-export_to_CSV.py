#!/usr/bin/python3
"""This module request data from
jsonplaceholder"""
import csv
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
        new_list.append([id, username, todo['completed'], todo['title']])
    file_name = '{}.csv'.format(id)
    with open(file=file_name, mode='w') as file:
        write = csv.writer(file, delimiter=',',
                           quotechar='"', quoting=csv.QUOTE_ALL)
        for rec in new_list:
            write.writerow(rec)
