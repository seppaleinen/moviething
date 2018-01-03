#!/usr/local/bin/python3

import sys, csv, re, string, click


@click.group()
def cli():
    """This application is for finding which movies in my imdb watchlist is not on my server"""


@cli.command('compare', short_help='Compare two files')
@click.argument('media_folder_path', metavar='<mediafolder-path>')
@click.argument('watchlist_path', metavar='<watchlist-path>')
def compare(media_folder_path, watchlist_path):
    """
    This will compare the already downloaded files

    \b
    find /Volumes/video/ -type d -wholename */hd-film/* -o -wholename */film/* -type d | grep -v 'Recycle' | sort > movies.txt
    curl -Qo- 'http://www.imdb.com/list/ls002936702/export' > watchlist.csv

    e.g:
    ./coolio.py compare ./movies.txt ./watchlist.csv
    """

    watchlist = parse_watchlist_data(watchlist_path)

    available_movies = parse_available_data(media_folder_path)

    diff = get_diff(available_movies, watchlist)
    for row in diff:
        print(row)
    return diff


def get_diff(available_movies, watchlist):
    return list(set(watchlist) - set(available_movies))


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
            watchlist.append(parse_data(title, year))

    return watchlist


def parse_data(title, year):
    return "%s - %s" % (normalize(title), year)


def normalize(s):
    for p in [".", "'", ":"]:
        s = s.replace(p, '')

    return s.lower().strip()


if __name__ == '__main__':
    cli()