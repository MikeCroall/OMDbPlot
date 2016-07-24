from colorama import init, Fore
from api import get_rating_of_year as arating, get_releases_in_year as areleases, get_popularity_of_year as apopularity
from files import get_rating_of_year as frating, get_releases_in_year as freleases, get_popularity_of_year as fpopularity

init(autoreset=True)


def get_rating_of_year(year, year_percent_string):
    from_file = frating(year, year_percent_string)
    return from_file if not from_file is None else arating(year, year_percent_string)


def get_releases_in_year(year, year_percent_string):
    from_file = freleases(year, year_percent_string)
    return from_file if not from_file is None else areleases(year, year_percent_string)


def get_popularity_of_year(year, year_percent_string):
    from_file = fpopularity(year, year_percent_string)
    return from_file if not from_file is None else apopularity(year, year_percent_string)

