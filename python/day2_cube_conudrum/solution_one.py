INPUT_FILE = "input.txt"
BAG_CONTENTS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

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


def validate_game(results: dict, specified_bag_contents: dict = None) -> dict:
    bag_contents = specified_bag_contents if specified_bag_contents else BAG_CONTENTS
    valid_results = results.copy()
    for game_id, game_results in results.items():
        game_is_valid = True
        for round in game_results:
            for result in round:
                if bag_contents[result[0]] < result[1]:
                    game_is_valid = False
                    break
        if not game_is_valid:
            valid_results.pop(game_id)
    return valid_results

parsed_game_results = parse_input()
valid_game_results = validate_game(parsed_game_results)
print(sum([key for key in valid_game_results.keys()]))




x = 0
