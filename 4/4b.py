def parse_card_data(line):
    parts = line.strip().split("|")
    winning_numbers = set(map(int, parts[0].split(":")[1].split()))
    user_numbers = set(map(int, parts[1].split()))
    return winning_numbers, user_numbers


def calculate_total_cards(cards):
    total_cards = 0
    card_copies = [1] * len(cards)  # Start with one copy of each card

    for i in range(len(cards)):
        winning_numbers, user_numbers = cards[i]
        matches = winning_numbers.intersection(user_numbers)
        num_matches = len(matches)
        # Distribute the copies to the next cards
        for j in range(i + 1, min(i + 1 + num_matches, len(cards))):
            card_copies[j] += card_copies[i]

    total_cards = sum(card_copies)
    return total_cards


file_path = "./4/input.txt"
with open(file_path, "r") as file:
    scratchcards_data = file.readlines()

parsed_cards = [parse_card_data(line) for line in scratchcards_data]

# Calculating the total number of scratchcards
print(calculate_total_cards(parsed_cards))
