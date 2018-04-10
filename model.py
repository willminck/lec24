#model.py
import csv

FB_FILE_NAME = 'umfootball.csv'

fb_seasons = []

def init_fball(csv_file_name=FB_FILE_NAME):
    global fb_seasons
    with open(csv_file_name) as f:
        reader = csv.reader(f)
        next(reader) # throw away headers
        next(reader) # throw away headers
        global fb_seasons
        fb_seasons = [] # reset, start clean
        for r in reader:
            r[3] = int(r[3])
            r[4] = int(r[4])
            r[5] = float(r[5])
            fb_seasons.append(r)

def get_fball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(fb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list
