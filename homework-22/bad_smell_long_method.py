csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list(data):
    data = _read(csv)
    data = _sort(data)
    return _filter(data)


def _read(csv):
    return [x.split(';') for x in csv.split('\n')]


def _sort(data):
    return sorted(data, key=lambda x: int(x[1]))


def _filter(data):
    return [x for x in data if int(x[1]) > 10]
