from src.secret import get_secret as key
# obviously, I'm keeping secret.py a secret, as it has my secret api_key.
# however, you can get your own over at https://www.themoviedb.org/documentation/api
# and simply return it from the method get_secret() in your own secret.py, isn't that great!?

api_key = key()
base_url = 'http://api.themoviedb.org/3/discover/movie?api_key={}&'.format(api_key)

import requests, time

def get_rating_of_year(year, year_percent_string):
    # preferably, do not print anything here, to avoid breaking progress showing nicely
    pages_in_year = -1
    try:
        # get pages
        r = requests.get(base_url + 'primary_release_year={}'.format(year))
        if r.status_code == requests.codes.ok:
            data = r.json()
            pages_in_year = data['total_pages']
        else:
            print("Not-ok status code returned: {}\nwhen finding pages in year {}".format(r.status_code, year))

        # iterate pages
        movie_ratings = []
        for page_num in range(1, pages_in_year + 1):
            print("\r\t\t{} - {:.2f}% complete...".format(year_percent_string, 100 * page_num / pages_in_year), end='')
            r = requests.get(base_url + 'primary_release_year={}&page={}'.format(year, page_num))
            if r.status_code == requests.codes.ok:
                page_data = r.json()
                movies = page_data['results']
                for movie in movies:
                    rating = movie['vote_average']
                    if rating != 0: # movies without ratings not counted
                        movie_ratings.append(rating)
                time.sleep(0.25) # try to avoid being timed out of api we are calling (MAX 40 calls per 10 seconds)
            else:
                print("Not-ok status code returned: {}\nwhen finding page {} in year {}".format(r.status_code, page_num, year))
        print("\r\t\t{} - done".format(year))

        # calculate result
        if len(movie_ratings) == 0:
            return -1
        return sum(movie_ratings) / len(movie_ratings)
    except:
        print("\n\n\t\tError - in finding rating of year {}\n\n".format(year))
        raise
    # todo can I somehow make querying any faster? Please?