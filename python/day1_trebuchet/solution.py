# Input data file name
INPUT_DATA = 'input.txt'

def is_int(possible_int: str) -> bool:
    """
    Try converting the provided string into an int.
    If a ValueError is rasied return False (the provided
    string could not be converted to an int), else return
    True (the value can be converted to an int)
    """
    try:
        int(possible_int)
    except ValueError:
        return False
    else:
        return True

with open(INPUT_DATA) as open_input_data:
    """
    Open the new line delimited text file and for each line, check if the character in
    the line can be converted to an integer value. If the value can be an int, keep it.
    This results in a list of lists. Each nested list is a record from the input, and
    will only contain strings that could be converted to ints. Then loop through that
    list of lists, and take the first and last string in each nested list, then combine
    them into a single string, convert that to an int, and lastly sum these ints
    """
    raw_data = open_input_data.readlines()
    int_strings_only = [[char for char in row if is_int(char)] for row in raw_data]
    cleaned_int_records = [int(f"{row[0]}{row[-1]}") for row in int_strings_only]
    print(sum(cleaned_int_records))
