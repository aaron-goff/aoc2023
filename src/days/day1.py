from helpers import read_file

input = read_file("day1")

num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
}

def is_not_negative(pair):
    _, value = pair
    return value >= 0

def clean_dict(dict_to_clean):
    return dict(filter(is_not_negative, dict_to_clean.items()))

def get_value_from_line(data):
    value = min(clean_dict(data), key=clean_dict(data).get)
    if value in num_dict.keys():
        return num_dict[value]
    else:
        return value

def get_start_and_end_number(input, use_string_numbers):
    total = 0
    found_nums = {}
    found_nums_reverse = {}
    for line in input:
        if use_string_numbers:
            for num in num_dict.keys():
                found_nums[num] = line.find(num)
                search = ""
                if num not in num_dict.keys():
                    search = num
                else:
                    search = num[::-1]
                found_nums_reverse[num] = line[::-1].find(search)
        for num in num_dict.values():
            found_nums[num] = line.find(num)
            found_nums_reverse[num] = line[::-1].find(num)

        total += int(get_value_from_line(found_nums) + get_value_from_line(found_nums_reverse))

    return total

print(get_start_and_end_number(input, False))
print(get_start_and_end_number(input, True))