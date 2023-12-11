import re


def is_symbol(char):
    return char not in (".", " ") and not char.isalnum()


def is_adjacent_to_symbol(grid, x, y, width, height):
    # Check adjacent cells including diagonally
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if is_symbol(grid[ny][nx]):
                    return True
    return False


with open("./3/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    height, width = len(lines), len(lines[0])
    total_sum = 0

    for y, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            number_start, number_end = match.span()
            # Check for adjacent symbols
            if any(
                is_adjacent_to_symbol(lines, x, y, width, height)
                for x in range(number_start, number_end)
            ):
                total_sum += int(match.group())

print(total_sum)
