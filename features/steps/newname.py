from behave import *

@given('righteousness')
def step_impl(context):
    pass

@when('time is right')
def step_impl(context):
    assert True is True

@then('we will rise!')
def step_impl(context):
    assert context.failed is False