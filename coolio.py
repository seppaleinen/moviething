#!/usr/local/bin/python3

import sys, csv, re, string


class Menu:
    def run(sys, argv):
        media_folder_path=argv[1]
        watchlist_path=argv[2]

        watchlist = parse_watchlist_data(watchlist_path)

        available_movies = parse_available_data(media_folder_path)

        return get_diff(available_movies, watchlist)


def get_diff(available_movies, watchlist):
    diff = []
    for wanted_movie in watchlist:
        match = None
        for available_movie in available_movies:
            if not match:
                if normalize(available_movie.title) == normalize(wanted_movie.title) and available_movie.year == wanted_movie.year:
                    match = available_movie
        if not match:
            print("MOVIE: %s not collected" % wanted_movie)
            diff.append(wanted_movie)
    return diff


def normalize(s):
    for p in [".", "'"]:
        s = s.replace(p, '')

    return s.lower().strip()


def parse_available_data(data):
    available_movies = []
    with open(data, 'r', encoding="utf-8") as myfile:
        for line in myfile.readlines():
            regex = re.search('^.*\/([\w.]+)\(([0-9]+)\)$', line, re.IGNORECASE)
            if regex:
                title=regex.group(1).replace(".", " ").replace("'", "")
                year=regex.group(2)
                available_movies.append(movie_data(id=None, title=title, year=year))
    return available_movies


def parse_watchlist_data(data):
    watchlist = []
    with open(data, 'r', encoding='iso-8859-1') as myfile:
        next(myfile) # Skip first line
        reader = csv.reader(myfile, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            id = row[1]
            title = row[5]
            year = row[10]
            watchlist.append(movie_data(id, title, year))

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