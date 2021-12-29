import os.path

import flask
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


def parsing_body(req):
    cmd1 = get_func(req['cmd1'])
    value1 = req['value1']
    cmd2 = get_func(req['cmd2'])
    value2 = req['value2']
    file_name = req['file_name']
    return cmd1, value1, cmd2, value2, file_name


def parsing_logs(req):
    cmd1, value1, cmd2, value2, file_name = parsing_body(req)
    data = []
    with open(f'{DATA_DIR}\\{file_name}', 'r') as f:
        file = f.readlines(8096)
        while file:
            file = cmd1(file, value1)
            file = cmd2(file, value2)
            data.append(''.join(file))
            file = f.readlines(8096)
    return data


@app.route('/perform_query', methods=['POST'])
def perform_query():
    req = request.json
    if len({'value1', 'value2', 'cmd1', 'cmd2', 'file_name'} and set(req)) != 5:
        return flask.jsonify(data='{"ERROR": "No body valid!"}'), 400
    if not os.path.exists(f'{DATA_DIR}\\{req["file_name"]}'):
        return flask.jsonify(data='{"ERROR": "No File name!"}'), 400
    response_data = parsing_logs(req)
    return app.response_class(''.join(response_data), content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
