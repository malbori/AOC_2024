from collections import defaultdict


def parse_input(file_path):
    with open(file_path, "r") as file:
        sections = file.read().strip().split("\n\n")
    rules_data = sections[0].split("\n")
    updates = sections[1].split("\n")

    # Parse rules into a defaultdict
    rules = defaultdict(list)
    for line in rules_data:
        a, b = line.split("|")
        rules[b].append(a)

    return rules, updates


def reorder(elements, rules):
    out = []
    while len(out) != len(elements):
        for e in elements:
            if e not in out:
                # Check if all dependencies are satisfied
                if all(x in out or x not in elements for x in rules[e]):
                    out.append(e)
                    break
    return out


def calculate_part1(updates, rules):
    p1 = 0
    for update in updates:
        pages = update.split(",")
        if pages == reorder(pages, rules):
            p1 += int(mid_item(pages))
    return p1


def calculate_part2(updates, rules):
    p2 = 0
    for update in updates:
        pages = update.split(",")
        reordered = reorder(pages, rules)
        if pages != reordered:
            p2 += int(mid_item(reordered))
    return p2


def mid_item(list_):
    return list_[len(list_) // 2]


def main():
    file_path = "solutions/day05/input.txt"
    rules, updates = parse_input(file_path)

    part1_result = calculate_part1(updates, rules)
    part2_result = calculate_part2(updates, rules)

    print("Part 1:", part1_result)
    print("Part 2:", part2_result)


if __name__ == "__main__":
    main()
