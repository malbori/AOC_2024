def process_input(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    left = []
    right = []

    for line in lines:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    return sorted(left), sorted(right)


def total_dist_calc(left_col, right_col):
    total_distance = 0
    for i in range(len(left_col)):
        left = left_col[i]
        right = right_col[i]

        if right >= left:
            distance = right - left
        else:
            distance = left - right
        # distance = r - l

        total_distance += distance

    return total_distance


def similarity_score_calc(left_col, right_col):
    counts = {}
    for i in right_col:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    similarity_score = 0
    for i in left_col:
        if i in counts:
            similarity_score += i * counts[i]

    return similarity_score


if __name__ == "__main__":
    left_sorted, right_sorted = process_input("solutions/day01/input.txt")
    total_distance = total_dist_calc(left_sorted, right_sorted)
    similarity_score = similarity_score_calc(left_sorted, right_sorted)
    print(total_distance)
    print(similarity_score)

    # print("Left column sorted:", left_sorted)
    # print("Right column sorted:", right_sorted)
