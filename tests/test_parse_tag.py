import pytest
from main import parse_tag


# юнит-тест на функцию. проверяю одну из функций, как она работает
def test_ok_one_class_one_id():
    data = "p.my-class#my-id"
    retval = parse_tag(data)
    assert retval == ["p", ["my-id"], ["my-class"]]


def test_ok_two_class_one_id():
    data = "p.my-class.my-class2#my-id"
    retval = parse_tag(data)
    assert retval == ["p", ["my-id"], ["my-class", "my-class2"]]


def test_ok_two_class_two_id():
    data = "p.my-class.my-class2#my-id#my-id2"
    retval = parse_tag(data)
    assert retval == ["p", ["my-id", "my-id2"], ["my-class", "my-class2"]]

# этот кейс считаю fail, потому что формат id через "#", а не через "."
def test_fail_two_class_two_id():
    data = "p.my-class.my-class2#my-id.my-id2"
    retval = parse_tag(data)
    assert retval == ["p", ["my-id.my-id2"], ["my-class", "my-class2"]]