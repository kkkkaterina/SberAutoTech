import json


def read_json(file_name: str) -> list:
    with open(file_name, "r") as read_file:
        data = json.load(read_file)
    return data


def do_html(data: list) -> None:
    result = ''
    for element in data:
        result += "<h1>" + element['title'] + "</h1>"
        result += "<p>" + element['body'] + "</p>"

    print_html(result)
    return None


def print_html(result: str) -> None:
    result_file = open('index.html', 'w')
    result_file.write(result)
    result_file.close()
    return None


if __name__ == '__main__':
    data = read_json('source1.json')
    #print(data)
    #print(type(data))
    do_html(data)
