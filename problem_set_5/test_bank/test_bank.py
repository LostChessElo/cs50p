from bank import value

def test_hello():
    assert value('hello') == 0

def test_h_greeting():
    assert value('hey') == 20
    assert value('how are you') == 20
    assert value('howdy') == 20
    assert value('hi') == 20


def test_other():
    assert value('1234') == 100
    assert value('whats up') == 100
    assert value('awe') == 100

def test_case_insensitivity():
    assert value('Hello') == 0
    assert value('Hi') == 20
    assert value('Any Other Greeting') == 100

