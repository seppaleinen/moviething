Feature: Check which movies I don't have that's in my IMDB watchlist

  Background:
    Given WATCHLIST.csv as watchlist
    And  MOVIES.txt as movielist
    When comparing

  Scenario Outline: If there's a movie in watchlist but none on computer
      Then this <expected> should be in the result

    Examples: Matches
      | expected                |
      |  Gandhi                 |
      # The comma messes things up
      #| Three Billboards Outside Ebbing, Missouri    |
      | Baadshaho               |
      | Padmavati               |
      | Happy Death Day         |
      | Kraftidioten            |

  Scenario Outline: If there's a match, and a diff show only diff
      Then this <expected> should not be in the result

    Examples: Matches
      | expected            |
      | The Doom Generation |
      | Zardoz              |
      | Schindler's List    |
      | The Elephant Man    |
      | Hunger              |
      | Black Dynamite      |
      | Seven Pounds        |
      | Le trou             |
      | Ran                 |
