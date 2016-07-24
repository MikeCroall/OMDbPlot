import requests, time
from colorama import init, Fore
from secret import get_secret as key
import files
init(autoreset=True)

# obviously, I'm keeping secret.py a secret, as it has my secret api_key.
# however, you can get your own over at https://www.themoviedb.org/documentation/api
# and simply return it from the method get_secret() in your own secret.py, isn't that great!?

api_key = key()
base_url = 'http://api.themoviedb.org/3/discover/movie?api_key={}&'.format(api_key)


def get_rating_of_year(year, year_percent_string):
    pages_in_year = -1
    # get pages
    r = requests.get(base_url + 'primary_release_year={}'.format(year))
    if r.status_code == requests.codes.ok:
        data = r.json()
        pages_in_year = data['total_pages']
    else:
        print(Fore.RED + "Not-ok status code returned: {} when finding pages in year {}".format(r.status_code, year))

    # iterate pages
    movie_ratings = []
    for page_num in range(1, pages_in_year + 1):
        try:
            print("\r\t\t{} - {:.2f}% complete...".format(year_percent_string, 100 * page_num / pages_in_year), end='')
            r = requests.get(base_url + 'primary_release_year={}&page={}'.format(year, page_num))
            if r.status_code == requests.codes.ok:
                page_data = r.json()
                movies = page_data['results']
                for movie in movies:
                    rating = movie['vote_average']
                    if rating != 0:  # movies without ratings not counted
                        movie_ratings.append(rating)
                time.sleep(0.26)  # try to avoid being timed out of api we are calling (MAX 40 calls per 10 seconds)
            else:
                print(Fore.RED + "Not-ok status code returned: {} when finding page {} in year {}".format(
                    r.status_code, page_num, year))
        except:
            print(Fore.RED + "\n\n\t\tError - in finding rating of year {}\n\n".format(year))
            raise
    print("\r\t\t{} - done                         ".format(year_percent_string))

    # calculate result
    if len(movie_ratings) == 0:
        return -1
    rating = sum(movie_ratings) / len(movie_ratings)
    files.save_rating(year, rating)
    return rating

def get_releases_in_year(year, year_percent_string):
    print('\t\t{}'.format(year_percent_string))
    count = 0
    try:
        # get pages
        time.sleep(0.26) # try to avoid being timed out of api we are calling (MAX 40 calls per 10 seconds)
        r = requests.get(base_url + 'primary_release_year={}'.format(year))
        if r.status_code == requests.codes.ok:
            data = r.json()
            count = data['total_results']
        else:
            print(Fore.RED + "Not-ok status code returned: {} when finding pages in year {}".format(r.status_code, year))
    except:
        print(Fore.RED + "\n\n\t\tError - in finding releases in year {}\n\n".format(year))
        raise
    finally:
        if count != 0:
            files.save_releases(year, count)
        return count


def get_popularity_of_year(year, year_percent_string):
    pages_in_year = -1
    # get pages
    r = requests.get(base_url + 'primary_release_year={}'.format(year))
    if r.status_code == requests.codes.ok:
        data = r.json()
        pages_in_year = data['total_pages']
    else:
        print(Fore.RED + "Not-ok status code returned: {} when finding pages in year {}".format(r.status_code, year))

    # iterate pages
    movie_popularities = []
    for page_num in range(1, pages_in_year + 1):
        try:
            print("\r\t\t{} - {:.2f}% complete...".format(year_percent_string, 100 * page_num / pages_in_year), end='')
            r = requests.get(base_url + 'primary_release_year={}&page={}'.format(year, page_num))
            if r.status_code == requests.codes.ok:
                page_data = r.json()
                movies = page_data['results']
                for movie in movies:
                    rating = movie['popularity']
                    if rating != 0:  # movies without popularity value not counted
                        movie_popularities.append(rating)
                time.sleep(0.26)  # try to avoid being timed out of api we are calling (MAX 40 calls per 10 seconds)
            else:
                print(Fore.RED + "Not-ok status code returned: {} when finding page {} in year {}".format(
                    r.status_code, page_num, year))
        except:
            print(Fore.RED + "\n\n\t\tError - in finding popularity of year {}\n\n".format(year))
            raise
    print("\r\t\t{} - done                         ".format(year_percent_string))

    # calculate result
    if len(movie_popularities) == 0:
        return -1
    popularity =  sum(movie_popularities) / len(movie_popularities)
    files.save_popularity(year, popularity)
    return popularity
