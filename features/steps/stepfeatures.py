from behave import given, when, then
from hamcrest import assert_that, contains, not_none, none, equal_to
from coolio import Menu
import os.path

@given('{text} as watchlist')
def given_watchlist_data(context, text):

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../" + text)

    context.watchlist_path = path


@given('{text} as movielist')
def given_available_data(context, text):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../" + text)

    context.movies_path = path


@when('comparing')
def step_impl3(context):
    context.result = Menu().run(["asd", context.movies_path, context.watchlist_path])


@then('this {expected} should be in the result')
def movies_should_be_in_result(context, expected):
    match = False
    for movie in context.result:
        match = match is not True and movie.title in expected.strip()

    assert_that(match, equal_to(True))


@then('this {expected} should not be in the result')
def movies_should_be_in_result(context, expected):
    match = any(x.title == expected for x in context.result)
    assert_that(match, equal_to(False))