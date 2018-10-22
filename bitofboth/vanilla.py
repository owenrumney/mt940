#!/bin/python

import json


def create_json(line, headers):
    data = {}
    row = line.rstrip().split(',')
    for i, header in enumerate(headers):
        data[header] = row[i]
    return json.dumps(data)


def main():
    with open('headers.txt', 'r') as f:
        headers = f.read().rstrip().split(',')

    with open('data.txt', 'r') as dr:
        for line in dr:
            print(create_json(line, headers))


if __name__ == '__main__':
    main()
