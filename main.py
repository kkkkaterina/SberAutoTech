import json
from typing import Union
import html


def read_json(file_name: str) -> list:
    with open(file_name, "r") as read_file:
        data = json.load(read_file)
    return data


def get_element_tags(element: dict) -> list:
    return list(element.keys())


def text_to_html(text: str) -> str:
    return html.escape(u"{}".format(text))


# p.my-class1.my-class2#id1#id2#id3 - формат
def parse_tag(input: str) -> [str, list, list]:
    tag_classes = input.split("#")[0]
    tag = tag_classes.split(".")[0]
    classes = tag_classes.split(".")[1:]
    try:
        ids = input.split("#")[1:]
    except IndexError:
        ids = []

    return [tag, ids, classes]


def id_class_to_text(param: list, name: str) -> str:
    param_text = "{}=\"".format(name) if len(param) > 0 else ""

    for count, element in enumerate(param):
        element = " " + str(element) if count > 0 else str(element)
        param_text += "{}".format(element)

    param_text += "\" " if len(param) > 0 else ""
    return param_text


def get_tag_params(input: str) -> [str, str]:
    tag, ids, classes = parse_tag(input)

    id_text = id_class_to_text(ids, "id")
    class_text = id_class_to_text(classes, "class")

    open_tag = "<{} ".format(tag) + id_text + class_text + ">"
    close_tag = "</{}>".format(tag)
    return [open_tag, close_tag]


def do_html_listed(data: list) -> str:
    # принимаю, что в json только list приходит и не может быть dict
    # коммент от HR: по 3 задаче: да для нее можно принять, что приходит список [] снаружи6 и внутри нет списков.
    result = ['<ul>']
    for element in data:
        result.append('<li>')
        for tag in get_element_tags(element):
            open_tag, close_tag = get_tag_params(tag)

            if isinstance(element[tag], list):
                result.append(open_tag + do_html_listed(element[tag]) + close_tag)
            else:
                result.append(open_tag + text_to_html(element[tag]) + close_tag)
        result.append('</li>')
    result.append('</ul>')
    return ''.join(result)


# на примере 5й задаче подумала, что все же надо сделать два случая:
# 1) json cо списком словарей
# 2) json со словарем
def do_html_dicted(data: dict) -> str:
    result = ['']
    for tag in data:
        open_tag, close_tag = get_tag_params(tag)
        if isinstance(data[tag], list):
            result.append(open_tag + do_html_listed(data[tag]) + close_tag)
        else:
            result.append(open_tag + text_to_html(data[tag]) + close_tag)
    return ''.join(result)


def make_html(data: Union[list, dict]) -> str:
    result = None
    if isinstance(data, list):
        result = do_html_listed(data)
    elif isinstance(data, dict):
        result = do_html_dicted(data)

    return result


def save_html(result: str) -> None:
    result_file = open('index.html', 'w')
    result_file.write(result)
    result_file.close()
    return None


if __name__ == '__main__':
    data = read_json('source6.json')
    save_html(make_html(data))
