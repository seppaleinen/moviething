#!/usr/local/bin/python3

from fuzzywuzzy import process, fuzz
import sys, csv, re, click, requests, os


@click.group()
def cli():
    """This application is for finding which movies in my imdb watchlist is not on my server"""


@cli.command('data', short_help='Get data')
@click.argument('imdb_user_id', metavar='<imdb_id>')
@click.argument('media_path', metavar='<media_path>')
def get_data(imdb_user_id, media_path):
    """
    This will fetch the data necessary for comparing

    e.g:
    ./coolio.py data ls002936702 /Volumes/video
    """

    get_media(media_path)
    download_watchlist(imdb_user_id)

    return None


def get_media(media_path):
    print('Getting media files')
    with open('media.txt', 'w') as output:
        for dirname, subdirs, files in os.walk(media_path):
            if len(subdirs) is 0 and len(files) is not 0:
                output.write(dirname + '\n')
    print('Media collecting complete')


def download_watchlist(imdb_user_id):
    headers = {'accept-encoding': 'identity'}
    url = 'http://www.imdb.com/list/%s/export' % imdb_user_id
    response = requests.get(url, stream=True, headers=headers)

    response_length=int(response.headers.get('content-length'))
    with click.progressbar(length=response_length, label="Downloading %s" % url) as bar:
        with open('watchlist.csv', 'wb') as output:
            for chunk in response.iter_content(chunk_size=1024 * 10):
                bar.update(len(chunk))
                output.write(chunk)



@cli.command('compare', short_help='Compare two files')
@click.option('--media', '-m', help='The path to the file with media data')
@click.option('--watchlist', '-w', default='./watchlist.csv', help='The path to the file with watchlist')
@click.option('--save-to-file', '-s', default='./media.txt', help='File to save result to')
def compare(media, watchlist, save_to_file):
    """
    This will compare the already downloaded files

    \b
    find /Volumes/video/ -type d -wholename */hd-film/* -o -wholename */film/* -type d | grep -v 'Recycle' | sort > movies.txt
    curl -Qo- 'http://www.imdb.com/list/ls002936702/export' > watchlist.csv

    e.g:
    ./coolio.py compare ./movies.txt ./watchlist.csv
    """

    watchlist = parse_watchlist_data(watchlist)

    available_movies = parse_available_data(media)

    diff = sorted(get_diff(available_movies, watchlist))

    if not save_to_file:
        for row in diff:
            print(row)
    else:
        with open(save_to_file, 'w') as file:
            for row in diff:
                file.write(row + '\n')

    return diff


def get_diff(available_movies, watchlist):
    first_diff = list(set(watchlist) - set(available_movies))

    diff = []
    with click.progressbar(first_diff, label='Comparing results') as bar:
        for wanted_movie in bar:
            result = process.extractOne(wanted_movie, available_movies, scorer=fuzz.token_set_ratio)
            if result[1] < 80:
                #print("RESULT FOR WANTED: %s - %s, %s" % (wanted_movie, result[0], result[1]))
                diff.append(wanted_movie)
    return diff


def parse_available_data(data):
    available_movies = []
    with open(data, 'r', encoding="utf-8") as myfile:
        for line in myfile.readlines():
            regex = re.search('^.*\/(.+)\(([0-9]+)\)$', line, re.IGNORECASE)
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
    cli()