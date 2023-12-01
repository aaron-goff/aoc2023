from src.days.day1 import *


def test_is_not_negative_true():
    pair = ('foo', 0)
    assert is_not_negative(pair) == True

def test_is_not_negative_false():
    pair = ('foo', -1)
    assert is_not_negative(pair) == False

def test_clean_dict():
    start = { 'foo': -1, 'bar': 0 }
    end = { 'bar': 0 }
    assert clean_dict(start) == end

def test_get_value_from_line_when_value_in_keys():
    start = { 'one': 10 }
    assert get_value_from_line(start) == '1'

def test_get_value_from_line_when_value_not_in_keys():
    start = { '1': 10 }
    assert get_value_from_line(start) == '1'

def test_get_start_and_end_number_when_use_strings_is_false():
    start = [ "1two3four5", "six7eight9", "sevenine10sevenine"]
    assert get_start_and_end_number(start, False) == 15 + 79 + 10

def test_get_start_and_end_number_when_use_strings_is_true():
    start = [ "1two3four5", "six7eight9", "sevenine10sevenine"]
    assert get_start_and_end_number(start, True) == 15 + 69 + 79
