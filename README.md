# Trying to get the diff of what movies I have, and which are in my watchlist

<a href="https://travis-ci.org/seppaleinen/moviething"><img src="https://travis-ci.org/seppaleinen/moviething.svg?branch=master" alt="Travis" /></a>


### Commands

```bash
#To run tests
behave

# Collect data
find /Volumes/video/ -type d -wholename */hd-film/* -o -wholename */film/* -type d | grep -v 'Recycle' | sort > movies.txt

# Collect watchlist
curl -Qo- 'http://www.imdb.com/list/ls002936702/export' > watchlist.csv

# To run script
./coolio.py /Users/david/workspace/moviething/movies.txt /Users/david/workspace/moviething/watchlist.csv 
```