from collections import defaultdict


def parse_input(filename):
    """
    Reads the input file and returns the grid and antenna positions by frequency.
    """
    grid = []
    nodes = defaultdict(list)
    with open(filename, "r") as file:
        for j, line in enumerate(file):
            line = line.strip()
            grid.append(line)
            for i, obj in enumerate(line):
                if obj != ".":
                    nodes[obj].append((i, j))
    return grid, nodes


def on_grid(pos, grid):
    """
    Checks if a position is within the boundaries of the grid.
    """
    m = len(grid)
    n = len(grid[0])
    return 0 <= pos[0] < n and 0 <= pos[1] < m


def find_antinodes(n1, n2):
    """
    Calculates the antinodes for a pair of antenna positions.
    """
    dx = n1[0] - n2[0]
    dy = n1[1] - n2[1]
    return [
        (n1[0] + dx, n1[1] + dy),  # Position beyond n1
        (n2[0] - dx, n2[1] - dy),  # Position beyond n2
    ]


def calculate_antinodes(nodes, grid):
    """
    Calculates all unique antinodes for antennas on the grid.
    """
    antinodes = []
    for frequency, positions in nodes.items():
        for n1, n2 in (
            (p, q) for i, p in enumerate(positions[:-1]) for q in positions[i + 1 :]
        ):
            antinodes.extend(find_antinodes(n1, n2))
    return {pos for pos in antinodes if on_grid(pos, grid)}


def main():
    grid, nodes = parse_input("solutions/day08/input.txt")

    # unique antinodes in grid
    unique_antinodes = calculate_antinodes(nodes, grid)

    print(f"Total: {len(unique_antinodes)}")


if __name__ == "__main__":
    main()
