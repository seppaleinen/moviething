Feature: Check which movies I don't have that's in my IMDB watchlist

  Background:
    Given WATCHLIST.csv as watchlist
    And  AVAILABLE_MOVIES.txt as movielist
    When comparing

  Scenario Outline: Show ones that are in watchlist but not movielist
      Then this <expected> should be in the result

    Examples: Matches
      | expected                                            |
      | "Gandhi - 1982"                                     |
      | "Three Billboards Outside Ebbing, Missouri - 2017"  |
      | "Baadshaho - 2017"                                  |
      | "Padmavati - "                                      |
      | "Happy Death Day - 2017"                            |
      | "Kraftidioten - 2014"                               |

  Scenario Outline: Matches should be case insensitive
      Then this <expected> should be in the result

    Examples: Matches
      | expected                                            |
      | "GANDHI - 1982"                                     |
      | "THREE BILLBOARDS OUTSIDE EBBING, MISSOURI - 2017"  |
      | "BAADSHAHO - 2017"                                  |
      | "PADMAVATI - "                                      |
      | "HAPPY DEATH DAY - 2017"                            |
      | "KRAFTIDIOTEN - 2014"                               |

  Scenario Outline: Do not show ones that are already in movielist
      Then this <expected> should not be in the result

    Examples: Matches
      | expected                      |
      | "The Doom Generation - 1995"  |
      | "Zardoz - 1974"               |
      | "Schindler's List - 1993"     |
      | "The Elephant Man - 1980"     |
      | "Hunger - 2008"               |
      | "Black Dynamite - 2009"       |
      | "Seven Pounds - 2008"         |
      | "Le trou - 1960"              |
      | "Ran - 1985"                  |
      | "spirited away - 2001"        |

  Scenario Outline: Do not show any that are only in movielist
      Then this <expected> should not be in the result

    Examples: Matches
      | expected                      |
      | "spirited away - 2001"        |
      | "strangers on a train - 1951" |
      | "contagion - 2011"            |
      | "rain man - 1988"             |
      | "pontypool - 2008"            |
      | "rogue one - 2016"            |
      | "the revenant - 2009"         |
    