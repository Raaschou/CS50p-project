import csv
import matplotlib as plt
import numpy as np

def main():
    # Get file path from user
    # Might be better to automate?
    #file_path = input("Input file path for csv file: ")

    titles, dates = get_info("NVH.csv")

    watched = list_watched_titles(titles)
    
    print(f"Unique titles watched: ", len(watched))
    
    for titles in watched:
        print(titles)


def get_info(netflix_view_hist):
    # Use DictReader to extract data from csv file
    # Encoding is workaround for error, that was not thrown when using cs50.dev
    with open(netflix_view_hist, encoding="utf-8") as csvfile:
        
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
    # Reorder list in order of viewing
    list_of_titles.reverse()
    
    for title in list_of_titles[1:]:

        split_title = title.split(":")
        title_keywords = ["Season", "Volume", "Series", "Limited Series"]
        
        # Skip missing data
        if split_title[0] == " ":
            continue

        # FIXME Only name of episode gets counted as unique
        # Assign part before the keyword
        if len(split_title) > 2: 
            for keyword in title_keywords:
                for part in split_title:
                    if keyword in part:
                        processed_title = ":".join(split_title[:split_title.index(part)]).strip()
            
            if processed_title not in watched:
                watched.append(processed_title)
        else:
            watched.append(title)
        
    
    

    with open("watched.txt", "w", encoding="utf-8") as file:
            
            count = 1
            for titles in watched:
                file.write(f"{count} - {titles}\n")
                count += 1
    return watched


if __name__ == "__main__":
    main()
