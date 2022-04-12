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

# O(n)


def pattern_search(seq, pattern):
    positions = set()
    pattern_len = len(pattern)

    left_index = 0
    rigth_index = pattern_len

    while rigth_index < len(seq):
        tmp = True
        for idx_pattern in range(pattern_len):
            if pattern[idx_pattern] != seq[left_index + idx_pattern]:
                tmp = False
                break

        if tmp == True:
            positions.add(left_index + pattern_len // 2)

        left_index = left_index + 1
        rigth_index = rigth_index + 1

    return positions

# 1 + 1 + 1 + 1 + (n-m) + (n-m) + (n-m)m + (n-m)m + (n-m)m + (n-m) + (n-m) + 1 =
# 5 + 5(n-m) + 3m(n-m) = m(n-m) =
# O(mn - m^2) - horsi je mn =>
# O(mn)
# n = len(seq), m = len(pattern)
# nemusi se rozepisovat, jen se podivat, kolikrat bezi nejvnitrnejsi cyklus


def binary_search(seq, num_to_find):
    left_index = 0
    right_index = len(seq) - 1

    while left_index <= right_index:
        middle = (left_index + right_index) // 2

        if seq[middle] == num_to_find:
            return middle

        elif seq[middle] < num_to_find:
            left_index = middle + 1

        elif seq[middle] > num_to_find:
            right_index = middle - 1

    return None

# n = 2^k - 1
# n + 1 = 2^k
# k = log(n+1) ... log o zakladu 2
# log(n) x log(1)
# O(log(n))


def main():
    unordered_numbers = read_data('sequential.json', 'unordered_numbers')
    print(unordered_numbers)

    dict_out = linear_search(unordered_numbers, 3)
    print(dict_out)

    dna_sequence = read_data('sequential.json', 'dna_sequence')
    positions = pattern_search(dna_sequence, "ATA")
    print(positions)

    ordered_numbers = read_data('sequential.json', 'ordered_numbers')
    idx_out = binary_search(ordered_numbers, 13)
    print(idx_out)


if __name__ == '__main__':
    main()