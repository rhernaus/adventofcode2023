# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

possible_games = 0
max_red = 12
max_green = 13
max_blue = 14

with open("./2/input.txt") as f:
    games = f.readlines()
    for game in games:
        impossible = False
        # Game 71: 10 blue, 6 green, 7 red; 5 red, 5 green, 2 blue; 7 green, 4 red, 5 blue; 1 red, 8 blue; 5 red, 1 blue, 8 green; 5 blue, 1 red, 5 green

        game_id = game.split(":")[0].strip().split(" ")[1].strip()
        print(f"Game {game_id}: ")

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

                if color == "red" and amount > max_red:
                    print(f"Impossible: {color} {amount}")
                    impossible = True
                elif color == "green" and amount > max_green:
                    print(f"Impossible: {color} {amount}")
                    impossible = True
                elif color == "blue" and amount > max_blue:
                    print(f"Impossible: {color} {amount}")
                    impossible = True

        if not impossible:
            possible_games += int(game_id)

print(possible_games)
