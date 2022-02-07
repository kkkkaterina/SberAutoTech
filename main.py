import json


def read_json(file_name: str) -> list:
    with open(file_name, "r") as read_file:
        data = json.load(read_file)
    return data


def get_element_tags(element: dict) -> list:
    return list(element.keys())


def do_html(data: list) -> str:
    # принимаю, что в json только list приходит и не может быть dict
    # коммент от HR: по 3 задаче: да для нее можно принять, что приходит список [] снаружи6 и внутри нет списков.
    result = ['<ul>']
    for element in data:
        result.append('<li>')
        for tag in get_element_tags(element):
            if isinstance(element[tag], list):
                result.append("<{}>".format(tag) + do_html(element[tag]) + "</{}>".format(tag))
            else:
                result.append("<{}>".format(tag) + element[tag] + "</{}>".format(tag))
        result.append('</li>')
    result.append('</ul>')
    return ''.join(result)


def save_html(result: str) -> None:
    result_file = open('index.html', 'w')
    result_file.write(result)
    result_file.close()
    return None


if __name__ == '__main__':
    data = read_json('source4.json')
    save_html(do_html(data))