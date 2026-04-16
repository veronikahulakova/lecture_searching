import json
import os
from operator import index
from generators import *
import time
import matplotlib.pyplot as plt

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
    left_idx = 0
    right_idx = len(sequence) - 1
    while left_idx != right_idx:
        middle_idx = round((right_idx + left_idx) / 2)
        if wanted == sequence[middle_idx]:
            return middle_idx

        if wanted > sequence[middle_idx]:
            left_idx = middle_idx + 1
        elif wanted < sequence[middle_idx]:
            right_idx = middle_idx - 1

    return None


def main():
    sequential_data = read_data('sequential.json', 'ordered_numbers')
    print(sequential_data)
    lengths = [100, 500, 1000, 5000, 10000]
    time_linear = []
    time_binary = []
    for length in lengths:
        generated_data = ordered_sequence(length)

        start_linear = time.perf_counter()
        linear_search(generated_data, length // 2)
        end_linear = time.perf_counter()
        duration_linear = end_linear - start_linear
        time_linear.append(duration_linear)

        start_binary = time.perf_counter()
        binary_search(generated_data, length // 2)
        end_binary = time.perf_counter()
        duration_binary = end_binary - start_binary
        time_binary.append(duration_binary)


    # time_linear.sort()
    # time_binary.sort()
    plt.plot(lengths, time_linear)
    plt.xlabel('pocet prvku v sekvenci')
    plt.ylabel('cas [s]')
    plt.title('graf casu behu linearniho vyhledavani')
    plt.show()
    plt.plot(lengths, time_binary)
    plt.xlabel('pocet prvku v sekvenci')
    plt.ylabel('cas [s]')
    plt.title('graf casu behu binarniho vyhledavani')
    plt.show()

if __name__ == '__main__':
    main()