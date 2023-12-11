import re


def find_part_numbers_around_star(grid, x, y, width, height):
    part_numbers = set()
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx].isdigit():
                # Extract the entire number, considering its extension
                left_bound = nx
                while left_bound > 0 and grid[ny][left_bound - 1].isdigit():
                    left_bound -= 1
                right_bound = nx
                while right_bound < width - 1 and grid[ny][right_bound + 1].isdigit():
                    right_bound += 1
                number = int(grid[ny][left_bound : right_bound + 1])
                part_numbers.add(number)
    return list(part_numbers)


with open("./3/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    height, width = len(lines), len(lines[0])
    total_gear_ratio_sum = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "*":
                part_numbers = find_part_numbers_around_star(lines, x, y, width, height)
                if len(part_numbers) == 2:
                    gear_ratio = part_numbers[0] * part_numbers[1]
                    total_gear_ratio_sum += gear_ratio
                    print(
                        f"Found gear ratio: Line {y + 1}, Column {x + 1}: {part_numbers[0]} * {part_numbers[1]} = {gear_ratio}"
                    )

print(f"Total gear ratio sum: {total_gear_ratio_sum}")
