def parse_input(file_path):
    """
    Parses the input file and constructs the `used` and `positions` arrays.
    """
    data = open(file_path).read().strip()
    used = []
    positions = []

    for i, ch in enumerate(data):
        if i % 2 == 0:
            used.extend([i // 2] * int(ch))
            positions.append((i // 2, int(ch)))
        else:
            used.extend([None] * int(ch))
            positions.append((None, int(ch)))

    # Log the arrays for debugging
    with open("debug_log.txt", "w") as f:
        f.write("Used Array:\n")
        f.write(f"{used}\n")
        f.write("Positions Array:\n")
        f.write(f"{positions}\n")

    return used, positions


def move_files(positions):
    """
    Simulates the movement of files on the disk based on the `positions` array.
    """
    disk = positions[:]
    last_fid, _ = disk[-1]

    # Process files from the last file ID to the first
    for fid in range(last_fid, -1, -1):
        # Find the index of the current file
        for i in range(len(disk)):
            t_fid, flen = disk[i]
            if t_fid == fid:
                break

        # Find a suitable position to insert the file
        for j in range(i):
            jfid, empty_blocks = disk[j]
            if jfid is not None:
                continue
            if flen <= empty_blocks:
                remain = empty_blocks - flen
                disk[j] = disk[i]
                disk[i] = (None, flen)

                if remain:
                    disk = disk[: j + 1] + [(None, remain)] + disk[j + 1 :]
                break

    # Log the moved disk for debugging
    with open("debug_log.txt", "a") as f:
        f.write("\nMoved Disk:\n")
        f.write(f"{disk}\n")

    return disk


def expand_disk(disk):
    """
    Expands the disk representation into a flat list for final calculations.
    """
    full = []
    for fid, flen in disk:
        full.extend([fid] * flen)

    # Log the expanded disk for debugging
    with open("debug_log.txt", "a") as f:
        f.write("\nExpanded Disk:\n")
        f.write(f"{full}\n")

    return full


def calculate_total(disk):
    """
    Calculates the total cost based on file positions on the disk.
    """
    total = 0
    for i, fid in enumerate(disk):
        if fid is not None:
            total += i * fid
    return total


# Main Execution
file_path = "solutions/day09/input.txt"
used, positions = parse_input(file_path)
final_disk = expand_disk(move_files(positions))
total_cost = calculate_total(final_disk)

print(total_cost)
