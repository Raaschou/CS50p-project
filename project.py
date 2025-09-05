import csv
import matplotlib as plt
import numpy as np

def main():
    # Get file path from user
    # Might be better to automate?
    #file_path = input("Input file path for csv file: ")

    titles, dates = get_info("NVH.csv")

    watched = list_watched_titles(titles)


def get_info(netflix_view_hist):
    # Use DictReader to extract data from csv file
    # Encoding is workaround for error, that was not thrown when using cs50.dev
    with open(netflix_view_hist, encoding="cp437") as csvfile:
        
        reader = csv.DictReader(csvfile)

        # Initialise titles and dates and append all
        titles = []
        dates = []
        for row in reader:
            titles.append(row['Title'])
            dates.append(row['Date'])


    return titles, dates



# Use function to get view by month or year, maybe days
def parse_date(date):
    month, day, year = date.split("/")
    return f"{year}-{month}-{day}"


def plot_shows_watched_by_month():


    plt.plot[dates]


# Use function to get all shows, maybe show repeat viewings
def list_watched_titles(list_of_titles):
    watched = []
    for title in list_of_titles:

        split_title = title.split(":")


        if split_title[0] not in watched:
            watched.append(split_title[0])

    return watched


if __name__ == "__main__":
    main()
