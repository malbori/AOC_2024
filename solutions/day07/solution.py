from itertools import product


def parse_input(filename):
    """
    Parse the input file and return a list of (target, nums) tuples.
    """
    equations = []
    with open(filename) as file:
        for line in file:
            target_str, nums_str = line.split(":")
            target = int(target_str.strip())
            nums = list(map(int, nums_str.strip().split()))
            equations.append((target, nums))
    return equations


def can_combine_to(target, nums, ops):
    result = nums[0]
    for i in range(1, len(nums)):
        if ops[i - 1] == "+":
            result += nums[i]
        elif ops[i - 1] == "*":
            result *= nums[i]
        elif ops[i - 1] == "||":
            result = int(str(result) + str(nums[i]))

    return result == target


def main():
    # Parse the input file
    equations = parse_input("solutions/day07/input.txt")

    # Define the possible operators
    ops = ["+", "*", "||"]

    total_calibration_result = 0

    # Check each equation
    for target, nums in equations:
        # Generate all possible oerations combos
        possible_ops = product(ops, repeat=len(nums) - 1)

        for ops_combination in possible_ops:
            if can_combine_to(target, nums, ops_combination):
                total_calibration_result += target
                break

    print(f"Total Calibration Result: {total_calibration_result}")


if __name__ == "__main__":
    main()
