INPUT_DATA = 'input.txt'

def is_int(possible_int: str) -> bool:
    try:
        int(possible_int)
    except ValueError:
        return False
    else:
        return True

with open(INPUT_DATA) as open_input_data:
    raw_data = open_input_data.readlines()
    int_strings_only = [[char for char in row if is_int(char)] for row in raw_data]
    cleaned_int_records = [int(f"{row[0]}{row[-1]}") for row in int_strings_only]
    print(sum(cleaned_int_records))
