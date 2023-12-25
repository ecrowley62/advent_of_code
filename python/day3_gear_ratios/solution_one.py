from collections.abc import Generator
from itertools import chain

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


def find_symbols(line: list[str]) -> list[int]:
    symbol_indices = []
    for count, char in enumerate(line):
        if char != "." and not is_int(char):
            symbol_indices.append(count)
    return symbol_indices




if __name__ == "__main__":
    problem_data = [row[1] for row in read_input_data()]
    symbols = identify_unique_symbols_in_data(problem_data)

    by_line_analysis = {}
    for count, line in enumerate(problem_data):
        by_line_analysis[count] = {
            "line_number": count,
            "symbol_indices": find_symbols(line),
        }

    for line_number in by_line_analysis.keys():
        all_symbol_indices_nested = []
        for target_line_number in range(line_number-1 if line_number != 0 else 0, line_number+2):
            all_symbol_indices_nested.append(by_line_analysis[target_line_number]['symbol_indices'])
        all_symbol_indices = list(chain.from_iterable(all_symbol_indices_nested))

        x = 0
    

    x = 0
