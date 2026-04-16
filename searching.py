import json
import os
from operator import index

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    if field not in data.keys():
        return None
    else:
        return data[field]


def linear_search(sequence, wanted):
    positions = []
    count = 0
    for i, number in enumerate(sequence):
        if number == wanted:
            positions.append(i)
            count += 1
    d = {'positions': positions, 'count' : count}
    return d


def binary_search(sequence, wanted):
    left = min(sequence)
    left_idx = sequence.index(left)
    right = max(sequence)
    right_idx = sequence.index(right)
    while left != right:
        middle_idx = round((right_idx + left_idx) / 2)
        middle = sequence[middle_idx]
        if wanted > middle:
            left = middle
            left_idx = middle_idx + 1
        elif wanted < middle:
            right = middle
            right_idx = middle_idx - 1
        if wanted == middle:
            return middle_idx
    return None


def main():
    sequential_data = read_data('sequential.json', 'ordered_numbers')
    print(sequential_data)
    print(linear_search(sequential_data, -3))
    print(binary_search(sequential_data, 90))


if __name__ == '__main__':
    main()