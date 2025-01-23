def parse_input(file_path):
    """
    Reads the input file and constructs the grid representation.
    """
    lines = open(file_path).read().splitlines()
    grid = [list(map(int, line)) for line in lines]

    # Log the grid for debugging
    with open("debug_log.txt", "w") as f:
        f.write("Grid:\n")
        f.write("\n".join("".join(map(str, row)) for row in grid))
        f.write("\n")

    return grid


def get_value(grid, y, x):
    """
    Retrieves the value at a specific grid location, or returns None if out of bounds.
    """
    if y < 0 or x < 0:
        return None
    try:
        return grid[y][x]
    except IndexError:
        return None


def bfs(grid, start, is_bfs1=True):
    """
    Performs a breadth-first search (BFS) on the grid.

    - `start`: The starting position (y, x).
    - `is_bfs1`: Flag to determine whether to use BFS1 or BFS2 logic.
    """
    cur = set([start]) if is_bfs1 else [start]
    for i in range(9):
        nxt = set() if is_bfs1 else []
        for y, x in cur:
            if get_value(grid, y, x) != i:
                continue
            for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ny, nx = y + dy, x + dx
                if is_bfs1:
                    nxt.add((ny, nx))
                else:
                    nxt.append((ny, nx))
        cur = nxt
    return sum(get_value(grid, y, x) == 9 for y, x in cur)


def calculate_total(grid, bfs_type="bfs1"):
    """
    Calculates the total number of 9s found via BFS1 or BFS2.

    - `bfs_type`: "bfs1" for BFS1 logic or "bfs2" for BFS2 logic.
    """
    h, w = len(grid), len(grid[0])
    total = 0
    for y in range(h):
        for x in range(w):
            total += bfs(grid, (y, x), is_bfs1=(bfs_type == "bfs1"))

    # Log the total for debugging
    with open("debug_log.txt", "a") as f:
        f.write(f"\nTotal ({bfs_type}): {total}\n")

    return total


# Main Execution
file_path = "solutions/day10/input.txt"
grid = parse_input(file_path)

# Calculate totals using BFS1 and BFS2
total_bfs1 = calculate_total(grid, bfs_type="bfs1")
print("Total BFS1:", total_bfs1)

total_bfs2 = calculate_total(grid, bfs_type="bfs2")
print("Total BFS2:", total_bfs2)
