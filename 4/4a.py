def parse_card_data(line):
    parts = line.strip().split("|")
    winning_numbers = set(map(int, parts[0].split(":")[1].split()))
    user_numbers = set(map(int, parts[1].split()))
    return winning_numbers, user_numbers


def calculate_points(cards):
    total_points = 0
    for winning_numbers, user_numbers in cards:
        matches = winning_numbers.intersection(user_numbers)
        if matches:
            # Points are calculated as 2^(number of matches - 1)
            total_points += 2 ** (len(matches) - 1)
    return total_points


file_path = "./4/input.txt"
with open(file_path, "r") as file:
    scratchcards_data = file.readlines()

parsed_cards = [parse_card_data(line) for line in scratchcards_data]

# Calculating the total points
print(calculate_points(parsed_cards))
