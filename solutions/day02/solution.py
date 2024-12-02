def process_input(file_path):
    levels = []

    with open(file_path, "r") as f:
        for line in f:
            numbers = list(map(int, line.split()))
            levels.append(numbers)

    return levels


def is_safe(level):

    def is_safe_level(level):
        is_increasing = True
        is_decreasing = True

        for i in range(len(level) - 1):
            rate = level[i + 1] - level[i]
            if rate == 0 or abs(rate) > 3:
                return False

            if rate < 0:
                is_increasing = False
            if rate > 0:
                is_decreasing = False

        return is_increasing or is_decreasing

    if is_safe_level(level):
        return True

    for i in range(len(level)):
        new_level = level[:i] + level[i + 1 :]
        if is_safe_level(new_level):
            return True

    return False


if __name__ == "__main__":
    levels = process_input("solutions/day02/input.txt")
    # print("levels:")
    # for i in levels:
    #     print(i)

    safe_counts = 0
    for level in levels:
        if is_safe(level):
            safe_counts += 1
    print("safe rows:", safe_counts)
