def parse_input(filename):
    with open(filename, "r") as file:
        data = file.read().strip()

    used_blocks = []
    # debugging to figure out what the hell is going on
    positions = []

    for i, char in enumerate(data):
        block_size = int(char)
        if i % 2 == 0:  # Even index -> actual blocks
            used_blocks.extend([i // 2] * block_size)
            positions.append((i // 2, block_size))
        else:  # Odd index -> empty spaces
            used_blocks.extend([None] * block_size)
            positions.append((None, block_size))

    # Log parsed data
    # with open("debug_log.txt", "w") as log_file:
    #     log_file.write("Parsed used array:\n")
    #     log_file.write(f"{used_blocks}\n\n")
    #     log_file.write("Parsed positions array:\n")
    #     log_file.write(f"{positions}\n")

    print("used blocks: ", len(used_blocks))
    # print("positions blocks: ", positions)

    return used_blocks, positions


def move_blocks(used):
    disk = used[:]
    for i in range(len(disk) - 1, -1, -1):  # Start at end
        if disk[i] is None:  # empty spaces
            continue
        for j in range(i):  # Find the lowest empty spot
            if disk[j] is None:
                disk[j], disk[i] = disk[i], None
                break
    return disk


def calculate_total(disk):
    total = 0
    for i, block in enumerate(disk):
        if block is not None:
            total += i * block
    return total


def main():
    used, _ = parse_input("solutions/day09/input.txt")

    # Move blocks and fill gaps
    disk = move_blocks(used)

    total = calculate_total(disk)
    print(total)


if __name__ == "__main__":
    main()
