import re


def process_input(file_path):
    with open(file_path, "r") as file:
        return file.read()


def parseInstructions(data):
    pattern = r"mul\((\d+),(\d+)\)"
    do_dont_pat = r"(do\(\)|don't\(\))"

    # Part 1 pattern match
    # matches = re.findall(pattern, data)

    # Part 2 patter match
    instructions = re.findall(f"{do_dont_pat}|{pattern}", data)

    # Part 1 return
    # return [(int(x), int(y)) for x, y in matches]

    enabled = True
    commands = []

    for i in instructions:
        if i[0]:
            if i[0] == "do()":
                enabled = True
            elif i[0] == "don't()":
                enabled = False
        elif i[1] and i[2] and enabled:
            x, y = int(i[1]), int(i[2])
            commands.append((x, y))

    return commands


def total_sum(instructions):

    total = 0
    for x, y in instructions:
        total += x * y
    return total


if __name__ == "__main__":
    input = "solutions/day03/input.txt"
    data = process_input(input)

    instructions = parseInstructions(data)

    result = total_sum(instructions)

    print("Total:", result)
