def process_input(file_path):
    with open(file_path, "r") as file:
        data = [line.strip() for line in file.readlines()]
    return data


def find_xmas(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (0, 1),  # E
        (0, -1),  # W
        (1, 0),  # S
        (-1, 0),  # N
        (1, 1),  # SE
        (-1, -1),  # NW
        (1, -1),  # SW
        (-1, 1),  # NE
    ]
    matches = []

    for row in range(rows):
        for col in range(cols):
            for x, y in directions:
                found = True
                for i in range(len(word)):
                    nr, nc = row + x * i, col + y * i
                    if (
                        nr < 0
                        or nr >= rows
                        or nc < 0
                        or nc >= cols
                        or grid[nr][nc] != word[i]
                    ):
                        found = False
                        break
                if found:
                    matches.append((row, col, x, y))
    return matches


def find_x_mas_patterns(grid):
    count = 0
    candidates = []
    row_len = len(grid)
    col_len = len(grid[0])

    for i in range(1, row_len - 1):
        for j in range(1, col_len - 1):
            if grid[i][j] == "A":
                candidates.append((i, j))

    for i, j in candidates:
        if (
            (grid[i - 1][j - 1] == "S" and grid[i + 1][j + 1] == "M")
            or (grid[i - 1][j - 1] == "M" and grid[i + 1][j + 1] == "S")
        ) and (
            (grid[i + 1][j - 1] == "S" and grid[i - 1][j + 1] == "M")
            or (grid[i + 1][j - 1] == "M" and grid[i - 1][j + 1] == "S")
        ):
            count += 1

    return count


def main():
    input = "solutions/day04/input.txt"
    grid = process_input(input)
    word = "XMAS"
    matches = find_xmas(grid, word)

    print(f"Matches found: {len(matches)}")
    # DEBUGGING
    # for i in matches:
    #     row, col, dr, dc = i
    # print(f"Match at row {row}, col {col} in direction ({dr}, {dc})")

    part2_count = find_x_mas_patterns(grid)

    print("Part 2 count: ", part2_count)


if __name__ == "__main__":
    main()
