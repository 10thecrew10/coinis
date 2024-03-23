from datetime import date
from typing import Callable

GENRES = ['Action', 'Crime', 'RPG', 'Fighting', 'Simulation', 'Survival', 'Horror']
ITEMS = ['name', 'rating', 'year', 'issuer', 'genre']


def validate_name(name: str):
    return 2 <= len(name) <= 50


def validate_rating(rating: str):
    try:
        float(rating)
    except:
        return False

    return 1 <= float(rating) <= 10 and (len((rating.split('.'))[-1]) == 1 or len(rating.split('.')) == 1)


def validate_year(year: str):
    try:
        int(year)
    except:
        return False

    return 1950 <= int(year) <= date.today().year


def validate_issuer(issuer: str):
    return 2 <= len(issuer) <= 40


def validate_genre(genre: str):
    gs = genre.split(' ')
    return 1 <= len(gs) <= 3 and all(True for x in gs if x in GENRES)


def validate_higher_param(higher: str):
    return higher.isdigit() and 0 <= int(higher) <= 1


def search_validator(text: str):
    return 1 <= len(text) <= 1024


def validate_using_function(func: Callable, field_name: str, text: str = None, optional: bool = False):
    if not text:
        text = field_name
    value = None
    if field_name == 'year' and text != 'year of issue':
        while True:
            value = input(f'Input {text}: ')
            if not (func(value)):
                print('Incorrect input. Try again.')
            else:
                res_dict = validate_using_function(validate_higher_param, 'higher',
                                        '[1] to find greater than entered year, otherwise [0]')
                return {field_name: value, 'higher': res_dict['higher']}
    elif optional:
        while True:
            value = input(f'Input {text} (Optional): ')
            if not (value):
                break
            elif not (func(value)):
                print('Incorrect input. Try again.')
            else:
                break
    else:
        while True:
            value = input(f'Input {text}: ')
            if not (func(value)):
                print('Incorrect input. Try again.')
            else:
                break
    return {field_name: value}


def validate_games(games: list):
    validated = []
    for game in games:
        if not (4 <= len(game) <= 5):
            continue
        if not validate_name(game[0]):
            continue
        if not validate_rating(game[1]):
            continue
        if not validate_year(game[2]):
            continue
        if len(game) == 5:
            if not validate_issuer(game[3]):
                continue
        if not validate_genre(game[-1]):
            continue

        validated.append(game)

    return validated


def filter_by_name(dict_to_filter: dict):
    return list(filter(lambda x: x[0].lower().startswith(dict_to_filter['name'].lower()), read_games()))


def filter_by_rating(dict_to_filter: dict):
    return list(filter(lambda x: float(x[1]) >= float(dict_to_filter['rating']), read_games()))


def filter_by_year(dict_to_filter: dict):
    if dict_to_filter['higher'] == '1':
        return list(filter(lambda x: int(x[2]) > int(dict_to_filter['year']), read_games()))
    return list(filter(lambda x: int(x[2]) <= int(dict_to_filter['year']), read_games()))


def filter_by_issuer(dict_to_filter: dict):
    res = []
    for elem in read_games():
        if len(elem) == 5 and elem[3].lower().startswith(dict_to_filter['issuer'].lower()) or \
                len(elem) == 4 and elem[2].lower().startswith(dict_to_filter['issuer'].lower()):
            res.append(elem)

    return res


def filter_by_genre(dict_to_filter: dict):
    genres_to_find = set(dict_to_filter['genre'].split())
    res = []
    for game in read_games():
        genres_of_game = set(game[-1].split())
        if len(genres_to_find.intersection(genres_of_game)) == len(genres_to_find):
            res.append(game)
    return res


def filter_by_value(index: int, key_val_to_filter: dict):
    item = ITEMS[index]
    if item == 'name':
        return filter_by_name(key_val_to_filter)
    elif item == 'rating':
        return filter_by_rating(key_val_to_filter)
    elif item == 'year':
        return filter_by_year(key_val_to_filter)
    elif item == 'issuer':
        return filter_by_issuer(key_val_to_filter)
    elif item == 'genre':
        return filter_by_genre(key_val_to_filter)


def read_games():
    with open('week-4/igrice.txt', 'r') as f:
        games = list(map(lambda x: x.replace('\n', '').split(';'), f.readlines()))
        return games


def print_validated_games():
    validated_games = validate_games(read_games())
    print('\n' + ''.join(str(x) + '\n' for x in validated_games))


def add_game_to_file(game: dict):
    with open('week-4/igrice.txt', 'a') as f:
        f.write('\n' + ';'.join(game.values()))


def yes_no_form(text_to_display: str) -> bool:
    user_response = input(text_to_display + ' [Y/n]: ')
    while True:
        if not (user_response) or user_response.lower() == 'y':
            return True
        elif user_response.lower() == 'n':
            break
        else:
            print('Incorrect input. Try again.')
            user_response = input(text_to_display + ' [Y/n]: ')
    return False


def numeric_form(items: list, text_to_display: str) -> int:
    print(text_to_display)
    print(f'[0] - EXIT')
    for i, elem in enumerate(items):
        print(f'[{i + 1}] - {elem}')
    user_response = input('Input option: ')
    while True:
        if user_response.isdigit() and int(user_response) == 0:
            return None
        elif 1 <= int(user_response) <= len(items):
            return int(user_response) - 1
        print('Incorrect input. Try again.')
        user_response = input('Input option: ')


if __name__ == "__main__":
    print_validated_games()
    resp = yes_no_form('Whould u like to append new game?')

    if resp:
        while resp:
            inputed_game = {}
            inputed_game['name'] = validate_using_function(validate_name, 'name')['name']
            inputed_game['rating'] = validate_using_function(validate_rating, 'rating', 'rating (from 1 to 10)')['rating']
            inputed_game['year'] = validate_using_function(validate_year, 'year', 'year of issue')['year']
            issuer = validate_using_function(validate_issuer, 'issuer', optional=True)
            if issuer:
                inputed_game['issuer'] = issuer['issuer']
            inputed_game['genre'] = validate_using_function(validate_genre, 'genre', f'GENRES {GENRES}')['genre']

            add_game_to_file(inputed_game)
            resp = yes_no_form('Whould u like to append new game?')

    resp = yes_no_form('Whould u like to search games by filter?')
    if resp:
        index = numeric_form(ITEMS, 'Choose option to filter by: ')
        while index is not None:
            value = None
            if ITEMS[index] == 'name':
                key_val_to_filter = validate_using_function(search_validator, ITEMS[index])
            if ITEMS[index] == 'rating':
                key_val_to_filter = validate_using_function(search_validator, ITEMS[index])
            if ITEMS[index] == 'year':
                key_val_to_filter = validate_using_function(search_validator, ITEMS[index])
            if ITEMS[index] == 'issuer':
                key_val_to_filter = validate_using_function(search_validator, ITEMS[index])
            if ITEMS[index] == 'genre':
                key_val_to_filter = validate_using_function(search_validator, ITEMS[index], f'GENRES {GENRES}')

            filtered = filter_by_value(index, key_val_to_filter)
            print('\n' + ''.join(str(x) + '\n' for x in filtered))
            index = numeric_form(ITEMS, 'Choose option to filter by: ')

    print('Program finished. Bye!')
