from random import randrange, randint, choice


# generating up to 20 random numbers(0-1000) so there's something to sort
data = sorted([randint(0, 1000) for item in range(randrange(20))])
print(f'Generated {len(data)} random numbers: {data}')
"""
Wanting to see both cases work without rerunning program ad infinitum 
uncomment target based on choice function and comment out the randint one
"""
target = randint(0, 1000)
# target = choice(data)
print(f"Looking for {target}")


def binary_search(data, target):  # take list as input, set left and right index

    left_index = 0
    right_index = len(data)-1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2  # find middle index and compare with wanted number

        # depending on comparison result, return index or keep slicing appropriate part of list with right or left index
        if data[middle_index] == target:
            return print(f"{target} found at index {middle_index}.")
        elif data[middle_index] > target:
            right_index = middle_index - 1
        elif data[middle_index] < target:
            left_index = middle_index + 1

    return print(f"{target} not found.")


binary_search(data, target)
