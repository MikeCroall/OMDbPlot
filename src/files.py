import json, os


def get_rating_of_year(year, year_percent_string):
    path = os.path.join(os.path.dirname(__file__), 'data/{}.json'.format(year))
    if not os.path.isfile(path): return None

    with open(path) as data_file:
        data = json.load(data_file)

    if not 'rating' in data.keys(): return None

    print('\t\t{} - loaded from file'.format(year_percent_string))
    return data['rating']


def get_releases_in_year(year, year_percent_string):
    path = os.path.join(os.path.dirname(__file__), 'data/{}.json'.format(year))
    if not os.path.isfile(path): return None

    with open(path) as data_file:
        data = json.load(data_file)

    if not 'releases' in data.keys(): return None

    print('\t\t{} - loaded from file'.format(year_percent_string))
    return data['releases']


def get_popularity_of_year(year, year_percent_string):
    path = os.path.join(os.path.dirname(__file__), 'data/{}.json'.format(year))
    if not os.path.isfile(path): return None

    with open(path) as data_file:
        data = json.load(data_file)

    if not 'popularity' in data.keys(): return None

    print('\t\t{} - loaded from file'.format(year_percent_string))
    return data['popularity']


def save_rating(year, rating):
    dir = os.path.join(os.path.dirname(__file__), 'data/')
    if not os.path.isdir(dir):
        os.makedirs(dir)

    path = os.path.join(dir, '{}.json'.format(year))
    data = {}
    if os.path.isfile(path):
        with open(path) as data_file:
            data = json.load(data_file)
    data['rating'] = rating

    with open(path, 'w') as data_file:
        json.dump(data, data_file)


def save_releases(year, releases):
    dir = os.path.join(os.path.dirname(__file__), 'data/')
    if not os.path.isdir(dir):
        os.makedirs(dir)

    path = os.path.join(dir, '{}.json'.format(year))
    data = {}
    if os.path.isfile(path):
        with open(path) as data_file:
            data = json.load(data_file)
    data['releases'] = releases

    with open(path, 'w') as data_file:
        json.dump(data, data_file)


def save_popularity(year, popularity):
    dir = os.path.join(os.path.dirname(__file__), 'data/')
    if not os.path.isdir(dir):
        os.makedirs(dir)

    path = os.path.join(dir, '{}.json'.format(year))
    data = {}
    if os.path.isfile(path):
        with open(path) as data_file:
            data = json.load(data_file)
    data['popularity'] = popularity

    with open(path, 'w') as data_file:
        json.dump(data, data_file)
