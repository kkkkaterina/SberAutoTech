import pytest
from main import make_html

# интеграционный тест. Проверяю, что моя программа полностью работает.
# для меня это показывает, работают ли все модули вместе в библиотеке main
# функцию save_html я решила не тестировать, потому что в ней стандартные функции.
def test_ok():
    data = {
        "p.my-class#my-id": "hello",
        "p.my-class1.my-class2": "example<a>asd</a>"
    }
    retval = make_html(data)
    assert retval == "<p id=\"my-id\" class=\"my-class\" >hello</p><p class=\"my-class1 my-class2\" >example&lt;a&gt;asd&lt;/a&gt;</p>"

def test_fail_id_end_space():
    data = {
        "p.my-class#my-id": "hello",
        "p.my-class1.my-class2": "example<a>asd</a>"
    }
    retval = make_html(data)
    assert not (retval == "<p id=\"my-id \" class=\"my-class\" >hello</p><p class=\"my-class1 my-class2\" >example&lt;a&gt;asd&lt;/a&gt;</p>")
