sum = 0
with open("./1/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        # find 1st digit
        for char in line:
            if char..isdigit():
                digits = str(char)
                break

        # find last digit
        for char in reversed(line):
            if char..isdigit():
                digits += str(char)
                break

        sum += int(digits)

print(sum)
