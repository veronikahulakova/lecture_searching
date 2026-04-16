import json
import os

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


def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')
    print(sequential_data)
    print(linear_search(sequential_data, 0))


if __name__ == '__main__':
    main()