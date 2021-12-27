import os.path
from flask import Flask, request

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route('/perform_query', methods=['POST'])
def perform_query():
    resp = request.json
    if not resp:
        return "No body request!", 400
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    file_name = resp['file_name']
    print(resp, file_name)
    if not os.path.exists(f'{DATA_DIR}\\{file_name}'):
        print(f'{DATA_DIR}\\{file_name}')
        return "No File name!", 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    file = get_logs(resp['file_name'])
    return app.response_class(f'{file}', content_type="text/plain")
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    # return app.response_class('', content_type="text/plain")


def get_logs(name):
    with open(f'{DATA_DIR}\\{name}', 'r') as f:
        return f


if __name__ == '__main__':
    app.run(debug=True)
