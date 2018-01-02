Feature: Check which movies I don't have that's in my IMDB watchlist

  Scenario: If there's a movie in watchlist but none on computer
     Given resources/WATCHLIST.csv as watchlist
      And  resources/movies.txt as movielist
      When comparing
      Then these movies should be in the result
        | movie  |
        | Zardoz |

  Scenario: If there's a match, and a diff show only diff
     Given resources/WATCHLIST2.csv as watchlist
      And  resources/movies2.txt as movielist
      When comparing
      Then these movies should be in the result
        | movie  |
        | Gandhi |


  Scenario: If there's a match, and a diff show only diff
     Given resources/WATCHLIST_DOOM.csv as watchlist
      And  resources/movies_DOOM.txt as movielist
      When comparing
      Then these movies should not be in the result
        | movie  |
        | The Doom Generation |

  Scenario: Check against all my movies
     Given resources/ACTUAL_WATCHLIST.csv as watchlist
      And  resources/allmovies.txt as movielist
      When comparing
      Then these movies should be in the result
        | movie  |
        | Gandhi |