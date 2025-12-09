# Intro to Search
# Author: Rachel
# 25 November

import csv


# Introduction to search algorithms
# Search for all songs for "Kendrick"
# Display all youtube and tiktok views
def main():
    # track name - 0
    # artist name - 2
    # youtube views - 11
    # tiktok views - 15
    song_name_col = 0
    artist_col = 2
    yt_views_col = 11
    tiktok_views_col = 15
    artist = "Kendrick Lamar"

    kendrick_songs = []

    # open the file
    with open("data/spotify2024.csv") as f:
        # get rid of the headr row
        _ = f.readline()
        # create a reader object
        r = csv.reader(f)

        for info in r:
            # if the current artist is "Kendrick"
            if info[artist_col] == artist:
                kendrick_songs.append(info)
        print(f"Number of Kendrick Songs: {len(kendrick_songs)}")

    #
    # read each line
    # print each line


if __name__ == "__main__":
    main()
