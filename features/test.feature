Feature: Check which movies I don't have that's in my IMDB watchlist

  Background:
    Given WATCHLIST.csv as watchlist
    And  MOVIES.txt as movielist
    When comparing

  Scenario Outline: If there's a movie in watchlist but none on computer
      Then this <expected> should be in the result

    Examples: Matches
      | expected                                  |
      | "Gandhi - 1982"                                    |
      | "Three Billboards Outside Ebbing, Missouri - 2017" |
      | "Baadshaho - 2017"                                 |
      | "Padmavati - "                                 |
      | "Happy Death Day - 2017"                           |
      | "Kraftidioten - 2014"                              |

  Scenario Outline: If there's a match, and a diff show only diff
      Then this <expected> should not be in the result

    Examples: Matches
      | expected            |
      | "The Doom Generation - 1995" |
      | "Zardoz - 1974"              |
      | "Schindler's List - 1993"    |
      | "The Elephant Man - 1980"    |
      | "Hunger - 2008"              |
      | "Black Dynamite - 2009"      |
      | "Seven Pounds - 2008"        |
      | "Le trou - 1960"             |
      | "Ran - 1985"                 |
