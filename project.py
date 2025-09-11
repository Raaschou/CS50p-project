import csv
import matplotlib.pyplot as plt
import matplotlib.dates  as mdates
import matplotlib.units as munits
import numpy as np
import pandas as pd
import datetime as dt

def main():
    # Get file path from user
    # Might be better to automate?
    #file_path = input("Input file path for csv file: ")

    titles, dates = get_info("NVH.csv")
   
    watched = list_watched_titles(titles)
    
    print(f"Unique titles watched: ", len(watched))
    plot_shows_watched_by_day(titles, dates)
    


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
    
    dates = parse_date(dates)
    
    return titles, dates



# Use function to get view by month or year, maybe days
# TODO Makes this using pandas?
def parse_date(dates):
    formatted_dates = []
    for date in dates:
        month, day, year = date.split("/")
        formatted_dates.append(f"20{year}-{month}-{day}")
    formatted_dates.reverse()
    return formatted_dates


def plot_shows_watched_by_day(titles, dates):
    
    # TODO Add days where nothing was watched
    unique_dates = []
    counts_per_date = []
    for date in dates:
            # if date == dates[len(dates)-1] and date in unique_dates:
            #     count_for_date += 1
            #     counts_per_date.append(count_for_date)
          
        if date in unique_dates:
            count_for_date += 1
        
        else:
            if unique_dates:
                counts_per_date.append(count_for_date)
            unique_dates.append(date)
            count_for_date = 1

    counts_per_date.append(count_for_date)
            
    
    print(len(unique_dates), " --- ", len(counts_per_date))
    
    
    # FIXME Put this someplace else
    plt.figure(figsize=(15, 8))
    plt.bar(unique_dates, counts_per_date,width=0.5)
    
    interval = max(1, len(unique_dates) // 20)  # Choose to show about 20 ticks
    plt.xticks(unique_dates[::interval], rotation=45)
    plt.xlabel('Dates')
    plt.ylabel('Episodes Watched')
    plt.title('Episode Watched by Month')
    plt.margins(0.0, 0) # TODO Decide margins
    #plt.tight_layout() 
    plt.savefig("test.png")

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
        # FIXME Some shows get season as well

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
