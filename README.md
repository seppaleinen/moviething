# Trying to get the diff of what movies I have, and which are in my watchlist

<a href="https://travis-ci.org/seppaleinen/moviething"><img src="https://travis-ci.org/seppaleinen/moviething.svg?branch=master" alt="Travis" /></a>
<a href='https://coveralls.io/github/seppaleinen/moviething?branch=master'><img src='https://coveralls.io/repos/github/seppaleinen/moviething/badge.svg?branch=master' alt='Coverage Status' /></a>


### Commands

```bash
#install requirements
pip3 install -r requirements
#To run tests
behave

#To run mutation tests
mutmut coolio.py --runner behave --tests-dir features/

# Collect data
find /Volumes/video/ -type d -wholename */hd-film/* -o -wholename */film/* -type d | grep -v 'Recycle' | sort > movies.txt

# Collect watchlist
curl -Qo- 'http://www.imdb.com/list/ls002936702/export' > watchlist.csv

# To run script
./coolio.py /Users/david/workspace/moviething/movies.txt /Users/david/workspace/moviething/watchlist.csv 
```