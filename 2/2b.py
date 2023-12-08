sum = 0

with open("./2/input.txt") as f:
    games = f.readlines()
    for game in games:
        min_red = 0
        min_green = 0
        min_blue = 0
        # Game 71: 10 blue, 6 green, 7 red; 5 red, 5 green, 2 blue; 7 green, 4 red, 5 blue; 1 red, 8 blue; 5 red, 1 blue, 8 green; 5 blue, 1 red, 5 green

        game_id = game.split(":")[0].strip().split(" ")[1].strip()
        print(f"Game {game_id}: ", end="")

        # Split games into hands

        hands = game.split(":")[1].strip()
        # 10 blue, 6 green, 7 red; 5 red, 5 green, 2 blue; 7 green, 4 red, 5 blue; 1 red, 8 blue; 5 red, 1 blue, 8 green; 5 blue, 1 red, 5 green

        hands = hands.split(";")
        # ['10 blue, 6 green, 7 red', ' 5 red, 5 green, 2 blue', ' 7 green, 4 red, 5 blue', ' 1 red, 8 blue', ' 5 red, 1 blue, 8 green', ' 5 blue, 1 red, 5 green']

        for hand in hands:
            # Split hand into cubes
            hand = hand.strip()

            cubes = hand.split(",")
            # ['10 blue', ' 6 green', ' 7 red']

            for cube in cubes:
                # Split cube into color and amount
                cube = cube.strip()  # 10 blue
                color = cube.split(" ")[-1]  # blue
                amount = int(cube.split(" ")[0])  # 10

                if color == "red" and amount > min_red:
                    min_red = amount
                elif color == "green" and amount > min_green:
                    min_green = amount
                elif color == "blue" and amount > min_blue:
                    min_blue = amount

        power = min_red * min_green * min_blue
        print(power)
        sum += power

print(sum)
