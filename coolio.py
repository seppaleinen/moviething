#!/usr/bin/python

import sys, csv, re


class Menu:
    def run(sys, argv):
        media_folder_path=argv[1]
        watchlist_path=argv[2]
        #print("Inputdata: {mediafolder_path:%s watchlist_path%s}" % (media_folder_path, watchlist_path))

        watchlist = parse_watchlist_data(watchlist_path)
        #print("WATCHLIST DATA: %s" % watchlist)

        available_movies = parse_available_data(media_folder_path)

        return get_diff(available_movies, watchlist)
        #print("DATA: %s" % available_movies)


def get_diff(available_movies, watchlist):
    diff=[]
    for wanted_movie in watchlist:
        match = None
        for available_movie in available_movies:
            if available_movie.title == wanted_movie.title and available_movie.year == wanted_movie.year:
                match = available_movie
        if not match:
            print("MOVIE: %s not collected" % wanted_movie)
            diff.append(wanted_movie)
    return diff


def parse_available_data(data):
    available_movies = []
    with open(data, 'r', encoding="utf-8") as myfile:
        for line in myfile.readlines():
            regex = re.search('^.*/([\w]+)\(([0-9]*)\)', line, re.IGNORECASE)
            if regex:
                title=regex.group(1).replace(".", " ")
                year=regex.group(2)
                available_movies.append(movie_data(id=None, title=title, year=year))
    return available_movies


def parse_watchlist_data(data):
    watchlist = []
    with open(data, 'r', encoding='iso-8859-1') as myfile:
        reader = csv.reader(myfile, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            id = row[1]
            title = row[5]
            year = row[10]
            watchlist.append(movie_data(id, title, year))

            #print("ID: %s, TITLE: %s, YEAR: %s" % (id, title, year))

    return watchlist


class movie_data():
    def __init__(self, id, title, year):
        self.id = id
        self.title = title
        self.year = year

    def __repr__(self):
        return "ID: %s TITLE: %s YEAR: %s" % (self.id, self.title, self.year)


if __name__ == '__main__':
    Menu().run(sys.argv)