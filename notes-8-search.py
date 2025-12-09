# Intro to Search
# Author: Rachel
# 25 November

import csv


# Introduction to search algorithms
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
    artist = "Sabrina Carpenter"

    Sabrina_songs = []

    # open the file
    with open("data/spotify2024.csv") as f:
        # get rid of the headr row
        _ = f.readline()
        # create a reader object
        r = csv.reader(f)

        # read each line of data
        for info in r:
            if info[artist_col] == artist:
                Sabrina_songs.append(info)
        print(f"Number of Sabrina Songs: {len(Sabrina_songs)}")

        for song in Sabrina_songs:
            current_track_name = song[song_name_col]
            current_yt_views = song[yt_views_col]
            current_tiktok_views = song[tiktok_views_col]
            # display information in a clear way
            # Squabble Up       100,000,000       120,000,000
            if 11 < len(current_track_name) > 15:
                tabs = "\t\t"
            elif 13 < len(current_track_name):
                num_tabs = 1
            else:
                num_tabs = 3

                print(
                    f"{current_track_name.strip()}{'\t' * num_tabs}{current_yt_views.strip()}{'\t' * num_tabs}{current_tiktok_views.strip()}"
                )

            # display info in a clear way

    #
    # read each line
    # print each line


if __name__ == "__main__":
    main()
