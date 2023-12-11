from collections.abc import Generator

INPUT_FILE = "input.txt"

def read_input_data() -> Generator[tuple[int, str], None, None]:
    with open(INPUT_FILE) as open_data_file:
        for line_num, raw_line in enumerate(open_data_file):
            yield line_num, raw_line.replace('\n','')

if __name__ == '__main__':
    problem_data = [row for row in read_input_data()]
    len(problem_data)