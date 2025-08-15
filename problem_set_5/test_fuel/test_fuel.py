from fuel import convert, gauge
import pytest

def main():
    test_input()
    test_0_div()
    test_val_error()

def test_input():
    assert convert('1/3') == 33 and gauge(33) == '33%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'

def test_0_div():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_val_error():
    with pytest.raises(ValueError):
        convert('cat/dog')
    with pytest.raises(ValueError):
        convert('1.3/3')
    with pytest.raises(ValueError):
        convert('5/3')
    with pytest.raises(ValueError):
        convert('-1/3')


if __name__ == '__main__':
    main()




