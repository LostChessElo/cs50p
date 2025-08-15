from plates import is_valid

def test_len():
    assert is_valid('A') == False
    assert is_valid('AA') == True
    assert is_valid('ABCEDF') == True
    assert is_valid('AAAAA123') == False

def test_startwith():
    assert is_valid('AA') == True
    assert is_valid('A1') == False
    assert is_valid('11') == False
    assert is_valid('1A') == False

def test_number_placement():
    assert is_valid('AAA12B') == False
    assert is_valid('AA01AB') == False
    assert is_valid('A1BC') == False

def test_zero():
    assert is_valid('AA12') == True
    assert is_valid('AA01') == False

def test_symbols():
    assert is_valid('AA..AA') == False
    assert is_valid('A?AA') == False



