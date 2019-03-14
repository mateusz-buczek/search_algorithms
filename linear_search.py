from random import randrange, randint, choice


# generating up to 20 random numbers(0-1000) so there's something to sort
data = [randint(0, 1000) for item in range(randrange(20))]
print(f'Generated {len(data)} random numbers: {data}')
"""
Wanting to see both cases work without rerunning program ad infinitum 
uncomment target based on choice function and comment out the randint one
"""
target = randint(0, 1000)
# target = choice(data)


def linear_sort(data, target):  # take data in form of list, and wanted number as arguments
    result = []  # create list collecting indices of searched number
    for index in range(len(data)):  # iterate through input data indices
        if data[index] == target:  # check if it matches searched number, add its index to list if it does
            result.append(index)

    if result:  # return created list, or "not found" if empty
        return print(f"{target} found in following indices: {result}.")
    else:
        return print(f"{target} not found in {data}.")


linear_sort(data, target)
