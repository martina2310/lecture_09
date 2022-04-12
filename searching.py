import os
import json

# get current working directory path (musi byt import os)
cwd_path = os.getcwd()


def read_data(file_name, field):  # (nazev souboru ze ktereho vytahujeme, konkretni ?promenna? kterou vytahujeme)

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as f:
        data = json.load(f)
    # osetreni (jestli je field v keys)
    if field in data.keys():
        return data[field]
    else:
        return None


def main():
    unordered_numbers = read_data('sequential.json', 'unordered_numbers')
    print(unordered_numbers)


if __name__ == '__main__':
    main()