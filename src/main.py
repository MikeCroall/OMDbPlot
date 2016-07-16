from src.api import get_rating_of_year as rating


def collect_data():
    d = {}
    start_year, end_year = 2006, 2010
    start_year, end_year = min(start_year, end_year), max(start_year, end_year)  # ensures correct way around
    total_years = end_year - start_year

    print("\tquerying from {} to {}".format(start_year, end_year))

    for year in range(start_year, end_year + 1):
        d[year] = rating(year, '{} ({:.2f}%)'.format(year, 100 * (year - start_year) / total_years))

    return d


def create_graph(plt, data):
    width = 0.5
    print("\tusing width {}".format(width))
    opacity = 0.4
    print("\tusing opacity {}".format(opacity))
    years = [i for i in data.keys()]
    ratings = [i for i in data.values()]
    plt.bar(years, ratings, width, color="green", align="center", alpha=opacity)
    plt.xticks(years, data.keys(), rotation='vertical')
    plt.xlabel('Year of release')
    plt.ylabel('Average rating over all films released during given year')
    plt.title('Average film rating (out of 10) by year of release')


def main():
    try:
        print("Importing libraries...")
        import matplotlib.pyplot as plt
        print("\tmatplotlib.pyplot imported")

        print("Gathering data...")
        data = collect_data()

        print("Creating graph...")
        create_graph(plt, data)

        print("Displaying graph...")
        plt.show()

    except:
        print("\n\n\t\tError - in main\n\n")
        raise


main()
