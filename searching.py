import os
import json

# get current working directory path (musi byt import os)
cwd_path = os.getcwd()


def read_data(file_name, field):  # (nazev souboru ze ktereho vytahujeme, konkretni ?promenna? kterou vytahujeme)

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as f:
        data = json.load(f)
    # osetreni (jestli je field v keys - aby fce vratila None pro vstupy, ktere nejsou v souboru):
    if field in data.keys():
        return data[field]
    else:
        return None


def linear_search(seq, num):
    positions = []
    count = 0

    for idx, val in enumerate(seq):
        if val == num:
            positions.append(val)
            count = count + 1

    dict_out = {
        "positions": positions,
        "count": count
    }
    return dict_out


def main():
    unordered_numbers = read_data('sequential.json', 'unordered_numbers')
    print(unordered_numbers)
    dict_out = linear_search(unordered_numbers, 3)
    print(dict_out)


if __name__ == '__main__':
    main()