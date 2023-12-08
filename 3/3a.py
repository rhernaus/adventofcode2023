# TODO: Code should check multi digit numbers instead of just single digits

symbols = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "_",
    "-",
    "+",
    "=",
    "[",
    "]",
    "{",
    "}",
    "|",
    ";",
    ":",
    "'",
    ",",
    "/",
    "?",
    "<",
    ">",
    "`",
    "~",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]

with open("./3/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        for char in line:
            if char.isdigit():
                # check if digit is adjecent to another digit or a symbol
                adjecent = False

                char_index = line.index(char)
                line_index = lines.index(line)

                # check previous line
                if line_index > 0:
                    prev_line = lines[line_index - 1]
                    # Check diagonal left above char
                    if char_index > 0:
                        if prev_line[char_index - 1] in symbols:
                            adjecent = True
                    # Check above char
                    if prev_line[char_index] in symbols:
                        adjecent = True
                    # Check diagonal right above char
                    if char_index < len(prev_line) - 1:
                        if prev_line[char_index + 1] in symbols:
                            adjecent = True

                # Check current line
                # Check left of char
                if char_index > 0:
                    if line[char_index - 1] in symbols:
                        adjecent = True
                # Check right of char
                if char_index < len(line) - 1:
                    if line[char_index + 1] in symbols:
                        adjecent = True

                # check next line
                if line_index < len(lines) - 1:
                    # Check diagonal left below char
                    if char_index > 0:
                        if lines[line_index + 1][char_index - 1] in symbols:
                            adjecent = True
                    # Check below char
                    if lines[line_index + 1][char_index] in symbols:
                        adjecent = True
                    # Check diagonal right below char
                    if char_index < len(lines[line_index + 1]) - 1:
                        if lines[line_index + 1][char_index + 1] in symbols:
                            adjecent = True

                if not adjecent:
                    print(char)
