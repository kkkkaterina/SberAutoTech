import json


def read_json(file_name: str) -> list:
    with open(file_name, "r") as read_file:
        data = json.load(read_file)
    return data


def get_element_tags(element: dict) -> list:
    return list(element.keys())


def do_html(data: list) -> None:
    # принимаю, что в json только list приходит и не может быть dict
    # коммент от HR: по 3 задаче: да для нее можно принять, что приходит список [] снаружи6 и внутри нет списков.
    result = '<ul>'
    for element in data:
        result += '<li>'
        for tag in get_element_tags(element):
            result += "<{}>".format(tag) + element[tag] + "</{}>".format(tag)
        result += '</li>'
    result += '</ul>'
    save_html(result)
    return None


def save_html(result: str) -> None:
    result_file = open('index.html', 'w')
    result_file.write(result)
    result_file.close()
    return None


if __name__ == '__main__':
    data = read_json('source3.json')
    # print(data)
    # print(type(data))
    do_html(data)
