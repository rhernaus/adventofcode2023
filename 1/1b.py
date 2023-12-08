import re

valid_digits = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
reversed_valid_digits = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "eno",
    "owt",
    "eerht",
    "ruof",
    "evif",
    "xis",
    "neves",
    "thgie",
    "enin",
]
sum = 0

# Create a pattern that matches any valid digit
pattern = re.compile("|".join(valid_digits))
reverse_pattern = re.compile("|".join(reversed_valid_digits))

with open("./1/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        # print line number
        print(f"{lines.index(line)+1}: ", end="")
        # find first valid digit in line
        match = pattern.search(line)
        if match:
            digit = match.group()
            # Convert written digits to numeric
            if digit.isalpha():
                digit = (
                    1
                    if digit == "one"
                    else 2
                    if digit == "two"
                    else 3
                    if digit == "three"
                    else 4
                    if digit == "four"
                    else 5
                    if digit == "five"
                    else 6
                    if digit == "six"
                    else 7
                    if digit == "seven"
                    else 8
                    if digit == "eight"
                    else 9
                )
                print("a", end="")
            digits = str(digit)
            print(digit, end="")

        # find last valid digit in line

        # reverse line
        reversed_line = line[::-1]

        match = reverse_pattern.search(reversed_line)
        if match:
            digit = match.group()
            # Convert written digits to numeric
            if digit.isalpha():
                digit = (
                    1
                    if digit == "eno"
                    else 2
                    if digit == "owt"
                    else 3
                    if digit == "eerht"
                    else 4
                    if digit == "ruof"
                    else 5
                    if digit == "evif"
                    else 6
                    if digit == "xis"
                    else 7
                    if digit == "neves"
                    else 8
                    if digit == "thgie"
                    else 9
                )
                print("a", end="")
            digits += str(digit)
            print(digit)

        sum += int(digits)

print(sum)
