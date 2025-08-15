from twttr import shorten

def test_twttr():
    assert shorten('hello') == 'hll'
    assert shorten('HELLO') == 'HLL'
    assert shorten('HElLo') == 'HlL'
    assert shorten('12345') == '12345'
    assert shorten('@!#$?') == '@!#$?'
