import matplotlib.pyplot as plt
from colorama import init, Fore
from api import get_rating_of_year as rating, get_releases_in_year as releases
init(autoreset=True)

options = {
    'ratings': {
        'title':"Average film rating (out of 10) by year of release",
        'xlabel':"Year of release",
        'ylabel':"Average rating over all films released during given year"
    },
    'release_count':{
        'title': "Total film release count by year",
        'xlabel': "Year of release",
        'ylabel': "Films released in given year"
    }
}


def choose_options():
    while True:
        print(Fore.GREEN + "Please choose a mode:")
        print(Fore.GREEN + "\t1 - average rating by year")
        print(Fore.GREEN + "\t2 - total releases by year")
        print(Fore.GREEN + "\t0 - exit")
        inp = input(Fore.GREEN + 'Choice: ')
        try:
            choice = int(inp)
            if choice == 1:
                return 'ratings'
            elif choice == 2:
                return 'release_count'
            elif choice == 0:
                return 'exit'
            else:
                print(Fore.RED + 'That is not a valid option number\n')
        except:
            print(Fore.RED + 'Please enter a valid integer option\n')


def collect_data(option):
    d = {}
    start_year, end_year = 2000, 2015
    start_year, end_year = min(start_year, end_year), max(start_year, end_year)  # ensures correct way around
    total_years = end_year - start_year

    print(Fore.LIGHTMAGENTA_EX + "\tquerying from {} to {}".format(start_year, end_year))

    for year in range(start_year, end_year + 1):
        if option == 'ratings':
            d[year] = rating(year, Fore.LIGHTMAGENTA_EX + '{} ({:.2f}%)'.format(year, 100 * (year - start_year) / total_years))
        elif option == 'release_count':
            d[year] = releases(year, Fore.LIGHTMAGENTA_EX + '{} ({:.2f}%)'.format(year, 100 * (year - start_year) / total_years))

    return d


def create_graph(data, option):
    width = 0.5
    print(Fore.LIGHTMAGENTA_EX + "\tusing width {}".format(width))
    opacity = 0.4
    print(Fore.LIGHTMAGENTA_EX + "\tusing opacity {}".format(opacity))
    years = [i for i in data.keys()]
    ratings = [i for i in data.values()]
    plt.bar(years, ratings, width, color="green", align="center", alpha=opacity)
    plt.xticks(years, data.keys(), rotation='vertical')
    plt.title(options[option]['title'])
    plt.xlabel(options[option]['xlabel'])
    plt.ylabel(options[option]['ylabel'])


def main():
    try:
        option = choose_options()
        if option == 'exit': return

        print(Fore.LIGHTMAGENTA_EX + "\nGathering data...")
        data = collect_data(option)

        print(Fore.LIGHTMAGENTA_EX + "Creating graph...")
        create_graph(data, option)

        print(Fore.LIGHTMAGENTA_EX + "Displaying graph...")
        plt.show()

    except:
        print("\n\n\t\tError - in main\n\n")
        raise


main()
