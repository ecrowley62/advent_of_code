from functools import reduce
import operator

INPUT_FILE = "input.txt"


def parse_input() -> dict[str : dict[str:int]]:
    game_results = {}
    with open(INPUT_FILE) as open_data_file:
        for raw_line in open_data_file:
            raw_game_id, raw_game_results = raw_line.replace("\n", "").split(":")
            game_id = int(raw_game_id.replace("Game ", ""))
            round_results = [
                [
                    (pull.split(" ")[1], int(pull.split(" ")[0]))
                    for pull in result.strip().split(", ")
                ]
                for result in raw_game_results.split(";")
            ]
            game_results[game_id] = round_results
    return game_results


def identify_min_required_cubes_per_game(
    game_results: dict,
) -> list[tuple[int, int, int]]:
    required_cubes_per_game = []
    for game in game_results.values():
        max_cubes = {"blue": 0, "red": 0, "green": 0}
        for round in game:
            for pull in round:
                max_cubes[pull[0]] = (
                    pull[1] if pull[1] > max_cubes[pull[0]] else max_cubes[pull[0]]
                )
        required_cubes_per_game.append(tuple([value for value in max_cubes.values()]))
    return required_cubes_per_game


def sum_power_of_cubes(min_cubes_required_identified: list) -> int:
    sum_powers = 0
    for min_cubes_for_game in min_cubes_required_identified:
        sum_powers += reduce(operator.mul, min_cubes_for_game)
    return sum_powers


input_data = parse_input()
required_cubes = identify_min_required_cubes_per_game(input_data)
result = sum_power_of_cubes(required_cubes)
print(result)
