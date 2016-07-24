import seaborn as sns
import matplotlib.pyplot as plt
import shutil, os
from colorama import init, Fore
from data import get_rating_of_year as rating, get_releases_in_year as releases, get_popularity_of_year as popularity

init(autoreset=True)

options = {
    'ratings': {
        'title': "Average film rating (out of 10) by year of release",
        'xlabel': "Year of release",
        'ylabel': "Average rating over all films released during given year"
    },
    'release_count': {
        'title': "Total film release count by year",
        'xlabel': "Year of release",
        'ylabel': "Films released in given year"
    },
    'popularity': {
        'title': "Average film popularity (out of 10) by year of release",
        'xlabel': "Year of release",
        'ylabel': "Average popularity over all films released during given year"
    }
}


def choose_options():
    while True:
        print("\n" + Fore.GREEN + "Please choose a mode:")
        print(Fore.GREEN + "\t1 - average rating by year")
        print(Fore.GREEN + "\t2 - total releases by year")
        print(Fore.GREEN + "\t3 - average popularity by year")
        print(Fore.GREEN + "\t9 - wipe locally saved data")
        print(Fore.GREEN + "\t0 - exit")
        inp = input(Fore.GREEN + 'Choice: ')
        try:
            choice = int(inp)
            if choice == 1:
                print("\nYou have chosen average rating by year")
                return 'ratings'
            elif choice == 2:
                print("\nYou have chosen total release count by year")
                return 'release_count'
            elif choice == 3:
                print("\nYou have chosen average popularity by year")
                return 'popularity'
            elif choice == 9:
                return 'wipe_local_data'
            elif choice == 0:
                return 'exit'
            else:
                print(Fore.RED + 'That is not a valid option number\n')
        except:
            print(Fore.RED + 'Please enter a valid integer option\n')


def get_valid_year(year_type):
    while True:
        inp = input(Fore.GREEN + "Please choose a {} year: ".format(year_type))
        try:
            choice = int(inp)
            if choice < 1800 or choice > 3000:  # no movies before 1800, no point querying too many future years with no movies yet
                print(Fore.RED + "Please enter a valid year to query\n")
            else:
                return choice
        except:
            print(Fore.RED + 'Please enter a valid integer year\n')


def collect_data(option, start, end):
    d = {}
    start_year, end_year = min(start, end), max(start, end)  # ensures correct way around
    total_years = end_year - start_year

    print(Fore.LIGHTMAGENTA_EX + "\tquerying from {} to {}".format(start_year, end_year))

    for year in range(start_year, end_year + 1):
        percentage = 100 if total_years == 0 else (100 * (year - start_year) / total_years)

        if option == 'ratings':
            d[year] = rating(year, Fore.LIGHTMAGENTA_EX + '{} ({:.2f}%)'.format(year, percentage))
        elif option == 'release_count':
            d[year] = releases(year, Fore.LIGHTMAGENTA_EX + '{} ({:.2f}%)'.format(year, percentage))
        elif option == 'popularity':
            d[year] = popularity(year, Fore.LIGHTMAGENTA_EX + '{} ({:.2f}%)'.format(year, percentage))

    return d


def create_graph(data, option):
    sns.set_style("whitegrid")
    bar_plot = sns.barplot(x=[y for y in data.keys()], y=[r for r in data.values()], color='palegreen')
    plt.xticks(rotation=90)
    plt.title(options[option]['title'])
    plt.xlabel(options[option]['xlabel'])
    plt.ylabel(options[option]['ylabel'])


def main():
    option = ''
    while option != 'exit':  # could be while true as exit returns from method, but is not for readability
        try:
            option = choose_options()

            if option == 'exit': return

            elif option == 'wipe_local_data':
                print(Fore.LIGHTRED_EX + "Wiping local data...")
                dir = os.path.join(os.path.dirname(__file__), 'data')
                if os.path.isdir(dir):
                    shutil.rmtree(dir)
                    print(Fore.LIGHTRED_EX + "Local data has been removed")
                else:
                    print(Fore.LIGHTRED_EX + "No local data found at {}".format(dir))
            else:
                start_year, end_year = get_valid_year('start'), get_valid_year('end')

                print(Fore.LIGHTMAGENTA_EX + "\nGathering data...")
                data = collect_data(option, start_year, end_year)

                print(Fore.LIGHTMAGENTA_EX + "Creating graph...")
                create_graph(data, option)

                print(Fore.LIGHTMAGENTA_EX + "Displaying graph...")
                plt.show()

        except KeyboardInterrupt as user_cancel:
            print('')
            pass
        except:
            print("\n\n\t\tError - in main\n\n")
            raise


main()
