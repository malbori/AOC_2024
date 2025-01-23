def parse_input(file_path):
    """
    Reads the input file and converts it into a list of integers.
    """
    with open(file_path, "r") as file:
        lines = file.read().strip().split()
    data = [int(x) for x in lines]

    # Log the input data for debugging
    # with open("debug_log.txt", "w") as log_file:
    #     log_file.write("Input Data:\n")
    #     log_file.write(f"{data}\n")

    return data


def update_stone(stone):
    """
    Processes a stone's value based on specific rules:
    - If the stone is 0, return (1,).
    - If the stone's value has an even number of digits, split it into two parts.
    - Otherwise, multiply the stone's value by 2024.
    """
    if stone == 0:
        return (1,)

    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        return (int(stone_str[:mid]), int(stone_str[mid:]))

    return (stone * 2024,)


def depth_first_search(mem, value, blinks):
    """
    Performs a depth-first search (DFS) to compute the result based on the stone's value and blinks left.
    - `mem`: A dictionary to memoize previously computed results.
    - `value`: The current value of the stone.
    - `blinks`: The number of blinks remaining.
    """
    if blinks == 0:
        return 1
    if (value, blinks) in mem:
        return mem[(value, blinks)]

    sub_values = update_stone(value)
    total = 0
    for sub_value in sub_values:
        total += depth_first_search(mem, sub_value, blinks - 1)

    mem[(value, blinks)] = total
    return total


def compute_total(data, blinks):
    """
    Calculates the total for all stones in the data using DFS with the given number of blinks.
    """
    mem = {}
    total = 0
    for stone in data:
        total += depth_first_search(mem, stone, blinks)

    # Log the computation details for debugging
    # with open("debug_log.txt", "a") as log_file:
    #     log_file.write(f"\nTotal for {blinks} blinks:\n")
    #     log_file.write(f"{total}\n")

    return total


def main():
    """
    Main execution function.
    """
    file_path = "solutions/day11/input.txt"
    data = parse_input(file_path)

    # Calculate results for 25 and 75 blinks
    result_25 = compute_total(data, 25)
    print("Result for 25 blinks:", result_25)

    result_75 = compute_total(data, 75)
    print("Result for 75 blinks:", result_75)


if __name__ == "__main__":
    main()
