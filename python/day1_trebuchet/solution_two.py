import re

# Input data file name
INPUT_DATA = "input.txt"

# Ints to int word mapping
NUM_TO_WORD_MAP = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

def identify_int_in_string(input_string: str, parse_from_end_of_string: bool = False) -> int:
    pattern = "|".join(NUM_TO_WORD_MAP.values()) + '|' + "|".join([str(key) for key in NUM_TO_WORD_MAP.keys()])
    for i in range(len(input_string)):
        section = input_string[-(i+1):] if parse_from_end_of_string else input_string[:i]
        match = re.findall(pattern, section)
        if match:
            try:
                return str(int(match[0]))
            except ValueError:
                for key, value in NUM_TO_WORD_MAP.items():
                    if match[0] == value:
                        return str(key)
            
with open(INPUT_DATA) as open_input_data:
    records_summed = 0
    all_records = []
    for record in open_input_data:
        first_int = identify_int_in_string(record)
        last_int = identify_int_in_string(record, parse_from_end_of_string=True)
        parsed_record_as_integer = f"{first_int if first_int else ''}{last_int if last_int else ''}"
        records_summed += int(parsed_record_as_integer)
    print(f"Answer is {records_summed}")
