from collections.abc import Generator

INPUT_FILE = "input.txt"


def read_input_data() -> Generator[tuple[int, str], None, None]:
    with open(INPUT_FILE) as open_data_file:
        for line_num, raw_line in enumerate(open_data_file):
            yield line_num, raw_line.replace("\n", "")


def is_int(char: str) -> bool:
    try:
        int(char)
    except ValueError:
        return False
    else:
        return True


def identify_unique_symbols_in_data(records: list[str]) -> list[str]:
    records_as_str = "".join(records).replace(".", "")
    return {char for char in records_as_str if not is_int(char)}


def find_numbers_adjacent_to_symbols(
    all_records: list[str],
    target_symbols: set[str],
    all_found_numbers: list[int] = None,
):
    if len(all_records) < 3:
        return all_found_numbers
    target_records = all_records[:3]
    del all_records[:3]

    parsed_records_info = []
    for rec_cnt, record in enumerate(target_records):
        symbol_indices, numbers, possible_number = [], [], []
        for char_cnt, char in enumerate(record):
            if char == ".":
                if possible_number:
                    number_parts, location_indices = [], []
                    for components in possible_number:
                        number_parts.append(components[0])
                        location_indices.append(components[1])
                    numbers.append(
                        {"num": int("".join(number_parts)), "ixs": location_indices}
                    )
                    possible_number.clear()
            elif char in target_symbols:
                symbol_indices.append(char_cnt)
            elif is_int(char):
                possible_number.append((char, char_cnt))
        parsed_records_info.append(
            {
                "record_num": rec_cnt,
                "found_numbers": numbers,
                "found_symbol_indices": symbol_indices,
            }
        )

    # TODO: Now that we have the three records with all numbers they contained identified,
    # including valid indices that touch the numbers, need to write a function that takes
    # these three records and returns the valid nums
    x = 0


if __name__ == "__main__":
    problem_data = [row[1] for row in read_input_data()]
    symbols = identify_unique_symbols_in_data(problem_data)
    valid_numbers = find_numbers_adjacent_to_symbols(problem_data, symbols)
