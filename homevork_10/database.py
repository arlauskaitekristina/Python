import datetime
import json
import csv

setup = 'setup.txt'
data_path = r'database'
indexes = []

def create_new() -> str:
    now = datetime.datetime.now()
    now = now.strftime("%d%m%Y")
    name = f'/{now}.csv'
    path = data_path + name
    with open(setup, 'w') as file:
        file.write(path)
    return path


def set_cols(cols) -> None:
    data = dict.fromkeys(cols)
    print(data)
    path = show_current()
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(data)


def show_current() -> str:
    with open(setup, 'r') as file:
        current_database = file.read()
    return current_database


def get_cols() -> []:
    with open(show_current(), 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        cols = reader.fieldnames
        return cols


def save_data(data) -> {}:
    cols = get_cols()
    with open(show_current(), 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=",", fieldnames=cols)
        writer.writerow({cols[0]: data[0], cols[1]: data[1], cols[2]: data[2]})
    return data


def show_base() -> None:
    rows = get_cols()
    print(rows)
    with open(show_current(), encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            print(f'{row[rows[0]]}, {row[rows[1]]}, {row[rows[2]]}')


def delete(numbers) -> None:
    """removal procedure. Uses cached_base for re-writing current db"""
    j = 1
    with open(show_current(), 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        with open('cache/cached_base.csv', 'w', newline='') as cache_file:
            writer = csv.writer(cache_file, delimiter=",")
            for row in reader:
                if j not in numbers:
                    writer.writerow(row)
                j += 1
    with open(show_current(), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        with open('cache/cached_base.csv', 'r', encoding='utf-8') as cache_file:
            reader = csv.reader(cache_file, delimiter=",")
            for row in reader:
                writer.writerow(row)


