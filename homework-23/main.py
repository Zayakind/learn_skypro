import os.path
import re
from dataclasses import dataclass
from typing import Optional, List, Set

import flask
import marshmallow.exceptions
import marshmallow_dataclass
from flask import Flask, request

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@dataclass
class RespParam:
    file_name: str
    cmd1: str
    cmd2: str
    value1: str
    value2: str


def get_func(cmd: str):
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
    if cmd == 'regex':
        return regex_line


def filtered(file, value: Optional[str]) -> List:
    return list(filter(lambda x: value in x, file))


def mapped(file, col: int) -> List[str]:
    col = int(col)
    return list(map(lambda line: line.split(' ')[col] if (len(line) > 3) else None, file))


def unique(file, pos) -> Set:
    return set(file)


def sort_file(file, desc: str) -> List[str]:
    if desc == 'asc':
        rever = True
    else:
        rever = False
    return sorted(file, reverse=rever)


def limit_line(file, limit) -> List[str]:
    limit = int(limit)
    return file[:limit+1]


def regex_line(file, reg_value: str) -> list[str]:
    return list(line for line in file if re.findall(reg_value, line))


def parsing_body(req: RespParam):
    cmd1 = get_func(req.cmd1)
    value1 = req.value1
    cmd2 = get_func(req.cmd2)
    value2 = req.value2
    file_name = req.file_name
    return cmd1, value1, cmd2, value2, file_name


def parsing_logs(req: RespParam) -> List[str]:
    cmd1, value1, cmd2, value2, file_name = parsing_body(req)
    data = []
    with open(f'{DATA_DIR}\\{file_name}', 'r') as f:
        file = f.readlines(8096)
        while file:
            if cmd1:
                file = cmd1(file, value1)
            if cmd2:
                file = cmd2(file, value2)
            data.append(' '.join(file))
            file = f.readlines(8096)
    return data


param = marshmallow_dataclass.class_schema(RespParam)


@app.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        req: RespParam = param().load(request.json)
    except marshmallow.ValidationError:
        return flask.jsonify(data='{"ERROR": "No body valid!"}'), 400
    response_data: List[str] = parsing_logs(req)
    return app.response_class(''.join(response_data), content_type="text/plain")


if __name__ == '__main__':
    app.run()
