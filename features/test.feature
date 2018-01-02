Feature: Check which movies I don't have that's in my IMDB watchlist

  Scenario Outline: If there's a movie in watchlist but none on computer
     Given <watchlist> as watchlist
      And  <movielist> as movielist
      When comparing
      Then this <expected> should be in the result

    Examples: Matches
      | watchlist                       | movielist                 | expected  |
      | resources/WATCHLIST.csv         | resources/movies.txt      | Zardoz    |
      | resources/WATCHLIST2.csv        | resources/movies2.txt     | Gandhi    |
      # The comma messes things up| resources/ACTUAL_WATCHLIST.csv  | resources/allmovies.txt   | Three Billboards Outside Ebbing, Missouri    |
      | resources/ACTUAL_WATCHLIST.csv  | resources/allmovies.txt   | Baadshaho    |
      | resources/ACTUAL_WATCHLIST.csv  | resources/allmovies.txt   | Padmavati    |
      | resources/ACTUAL_WATCHLIST.csv  | resources/allmovies.txt   | Happy Death Day    |
      | resources/ACTUAL_WATCHLIST.csv  | resources/allmovies.txt   | Kraftidioten    |

  Scenario Outline: If there's a match, and a diff show only diff
     Given <watchlist> as watchlist
      And  <movielist> as movielist
      When comparing
      Then this <expected> should not be in the result

    Examples: Matches
      | watchlist                         | movielist                     | expected            |
      | resources/WATCHLIST_DOOM.csv      | resources/movies_doom.txt     | The Doom Generation |
      | resources/ACTUAL_WATCHLIST.csv    | resources/allmovies.txt       | Schindler's List |
      | resources/ACTUAL_WATCHLIST.csv    | resources/allmovies.txt       | The Elephant Man |
      | resources/ACTUAL_WATCHLIST.csv    | resources/allmovies.txt       | Hunger |
      | resources/ACTUAL_WATCHLIST.csv    | resources/allmovies.txt       | Black Dynamite |
      | resources/ACTUAL_WATCHLIST.csv    | resources/allmovies.txt       | Seven Pounds |
      | resources/ACTUAL_WATCHLIST.csv    | resources/allmovies.txt       | Le trou |
      | resources/ACTUAL_WATCHLIST.csv    | resources/allmovies.txt       | Ran |
