#!/usr/local/bin/python3

import sys, csv, re, string
from fuzzywuzzy import process, fuzz


class Menu:
    def run(self, media_folder_path, watchlist_path):

        watchlist = parse_watchlist_data(watchlist_path)

        available_movies = parse_available_data(media_folder_path)

        diff = get_diff(available_movies, watchlist)
        for row in diff:
            print(row)
        return diff


def get_diff(available_movies, watchlist):
    first_diff = list(set(watchlist) - set(available_movies))

    rest_available_movies = list(set(available_movies) - set(watchlist))
    diff = []
    for wanted_movie in first_diff:
        result = process.extractOne(wanted_movie, rest_available_movies, scorer=fuzz.token_sort_ratio)
        #print("RESULT FOR WANTED: %s - %s, %s" % (wanted_movie, result[0], result[1]))
        if result[1] < 85:
            diff.append(wanted_movie)
        else:
            rest_available_movies.remove(result[0])
    return diff


def parse_available_data(data):
    available_movies = []
    with open(data, 'r', encoding="utf-8") as myfile:
        for line in myfile.readlines():
            regex = re.search('^.*\/([\w.]+)\(([0-9]+)\)$', line, re.IGNORECASE)
            if regex:
                title=regex.group(1).replace(".", " ")
                year=regex.group(2)
                available_movies.append(parse_data(title=title, year=year))
    return available_movies


def parse_watchlist_data(data):
    watchlist = []
    with open(data, 'r', encoding='iso-8859-1') as myfile:
        reader = csv.DictReader(myfile)
        for row in reader:
            title = row["Title"]
            year = row["Year"]
            watchlist.append(parse_data(title=title, year=year))

    return watchlist


def parse_data(title, year):
    return "%s - %s" % (normalize(title), year)


def normalize(s):
    for p in [".", "'", ":"]:
        s = s.replace(p, '')

    return s.lower().strip()


if __name__ == '__main__':
    media_folder_path=sys.argv[1]
    watchlist_path=sys.argv[2]

    Menu().run(media_folder_path, watchlist_path)