from collections import deque


def parse_input(file_path):
    with open(file_path, "r") as file:
        grid = file.read().splitlines()
    return grid


def get_start(grid):
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "^":
                return i, j
    return None


def traverse_grid(grid, sx, sy):
    adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    idx = 0
    q = deque([(sx, sy, idx)])

    while q:
        x, y, idx = q.popleft()
        dx, dy = adj[idx]
        visited.add((x, y))

        # Check boundary
        if not (0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0])):
            break

        # Check obstacle
        if grid[x + dx][y + dy] == "#":
            # Turn right
            idx = (idx + 1) % len(adj)
            q.append((x, y, idx))
        else:
            # Move
            q.append((x + dx, y + dy, idx))

    return visited


def calculate_obstructions(grid, visited, sx, sy):
    adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    num_obstructions = 0

    for i, j in visited:
        # check starting point
        if i == sx and j == sy:
            continue

        # Simulate traverse
        temp_visited = set()
        idx = 0
        q = deque([(sx, sy, idx)])

        while q:
            x, y, idx = q.popleft()
            dx, dy = adj[idx]

            if (x, y, idx) in temp_visited:
                num_obstructions += 1
                break

            temp_visited.add((x, y, idx))

            # Check boundary
            if not (0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0])):
                break

            # Check obstacle or ignoring cell
            if grid[x + dx][y + dy] == "#" or (x + dx == i and y + dy == j):
                # Turn right
                idx = (idx + 1) % len(adj)
                q.append((x, y, idx))
            else:
                # Move
                q.append((x + dx, y + dy, idx))

    return num_obstructions


def main():
    # Input file
    file_path = "solutions/day06/input.txt"
    grid = parse_input(file_path)

    # Get starting position
    sx, sy = get_start(grid)

    # Part 1: Find visited cells
    visited = traverse_grid(grid, sx, sy)
    print("Number of visited cells:", len(visited))

    # Part 2: Calculate obstructions
    num_obstructions = calculate_obstructions(grid, visited, sx, sy)
    print("Number of obstructions:", num_obstructions)


if __name__ == "__main__":
    main()
