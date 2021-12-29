import json
import os.path
from flask import Flask, request

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def get_func(cmd):
    if cmd == 'filter':
        return filtered
    if cmd == 'map':
        return mapped
    if cmd == 'unique':
        return unique
    if cmd == 'sort':
        return sort_file
    if cmd == 'limit':
        return limit_line


def filtered(file, value):
    return list(filter(lambda x: value in x, file))


def mapped(file, col):
    col = int(col)
    return list(map(lambda line: line.split(' ')[col] if (len(line) > 3) else None, file))


def unique(file, pos):
    return set(file)


def sort_file(file, desc):
    if desc == 'asc':
        desc = True
    else:
        desc = False
    return sorted(file, reverse=desc)


def limit_line(file, limit):
    limit = int(limit)
    return file[:limit+1]


@app.route('/perform_query', methods=['POST'])
def perform_query():
    req = request.json
    if not req:
        return json.dumps('{"error": "No body request!"}'), 400
    cmd1 = get_func(req['cmd1'])
    value1 = req['value1']
    cmd2 = get_func(req['cmd2'])
    value2 = req['value2']
    file_name = req['file_name']
    if not os.path.exists(f'{DATA_DIR}\\{file_name}'):
        return json.dumps('{"error": "No File name!"}'), 400
    response_data = []
    with open(f'{DATA_DIR}\\{file_name}', 'r') as f:
        file = f.readlines(8096)
        while file:
            file = cmd1(file, value1)
            file = cmd2(file, value2)
            response_data.append(''.join(file))
            file = f.readlines(8096)
        return app.response_class(''.join(response_data), content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
