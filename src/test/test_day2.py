from src.days.day2 import * 

def test_get_id_from_line():
    line = "Game 52: 12 blue, 8 red; 11 green, 9 red, 11 blue; 8 blue, 5 green, 8 red; 3 red, 11 blue, 11 green; 12 blue, 6 green, 5 red; 10 red, 8 green"
    assert get_id_from_line(line) == 52

def test_get_draws_as_list():
    line = "Game 52: 12 blue, 8 red; 11 green, 9 red, 11 blue; 8 blue, 5 green, 8 red; 3 red, 11 blue, 11 green; 12 blue, 6 green, 5 red; 10 red, 8 green"
    assert get_draws_as_list(line) == ["12 blue", "8 red", "11 green", "9 red", "11 blue", "8 blue", "5 green", "8 red", "3 red", "11 blue", "11 green", "12 blue", "6 green", "5 red", "10 red", "8 green"]

def test_get_max_in_line():
    line = "Game 52: 12 blue, 8 red; 11 green, 9 red, 11 blue; 8 blue, 5 green, 8 red; 3 red, 11 blue, 11 green; 12 blue, 6 green, 5 red; 10 red, 8 green"
    assert get_max_in_line(line) == { 'blue': 12, 'red': 10, 'green': 11 }

def test_is_possible_false():
    line = "Game 52: 12 blue, 8 red; 11 green, 9 red, 11 blue; 8 blue, 5 green, 8 red; 3 red, 11 blue, 11 green; 12 blue, 6 green, 5 red; 10 red, 8 green"
    max = { 'blue': 11, 'red': 9, 'green': 10 }
    assert is_possible(line, max) == False

def test_is_possible_true():
    line = "Game 52: 12 blue, 8 red; 11 green, 9 red, 11 blue; 8 blue, 5 green, 8 red; 3 red, 11 blue, 11 green; 12 blue, 6 green, 5 red; 10 red, 8 green"
    max = { 'blue': 13, 'red': 11, 'green': 12 }
    assert is_possible(line, max) == True

def test_get_total():
    lines = ["Game 1: 1 blue; 2 green", "Game 2: 2 red, 3 green", "Game 3: 5 blue; 1 red"]
    max = { "blue": 5, "red": 1, "green": 2 }
    assert get_total(lines, max) == 4

def test_get_power():
    lines = ["Game 1: 1 blue; 2 green; 3 red", "Game 2: 2 red, 3 green; 2 blue", "Game 3: 5 blue; 1 red, 3 green"]
    assert get_power(lines) == ((1 * 2 * 3) + (2 * 3 * 2) + (5 * 1 * 3))