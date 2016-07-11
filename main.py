def collect_data():
    import random  # todo remove
    d = {}
    start_year, end_year = 1950, 2017  # ensures all relevant titles, basically
    print("\tquerying from {} to {}".format(start_year, end_year))
    for year in range(start_year, end_year + 1):
        # todo api call to get list of ratings, average them
        d[year] = random.randint(0, 100)

    # data automatically displays in order because of the nature of the dictionary
    # do not worry about sorting at any point
    return d


def create_graph(plt, data):
    width = 0.5
    print("\tdisplaying with width {}".format(width))
    opacity = 0.4
    print("\tdisplaying with opacity {}".format(opacity))
    years = [i for i in data.keys()]
    ratings = [i for i in data.values()]
    plt.bar(years, ratings, width, color="green", align="center", alpha=opacity)
    plt.xlabel('Year')
    plt.ylabel('Average rating over all films from given year')
    plt.title(
        'Average film rating (out of {}) by year of release'.format('{{placeholder}}'))  # todo replace placeholder
    plt.xticks(years, data.keys(), rotation='vertical')


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

    except Exception as ex:
        print("\n\n\t\tError\n\n")
        raise


main()
