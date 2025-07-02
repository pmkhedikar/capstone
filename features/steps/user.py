from behave import when, then
from utils.api_helper import APIClient

@when('user send a GET request to "{endpoint}"')
def step_impl(context, endpoint):
    # Initialize API client if not already present
    if not hasattr(context, "api_client"):
        context.api_client = APIClient()
    context.response = context.api_client.get(endpoint)
    context.response_json = context.response.json()

@then('the response code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status == status_code, f"Expected {status_code}, got {context.response.status}"

@then('the user details should be present:')
def step_impl(context):
    expected = context.table[0]  # Only one row in your example
    actual = context.response_json["data"]
    assert actual["email"] == expected["email"], f"Expected email {expected['email']}, got {actual['email']}"
    assert actual["first_name"] == expected["first_name"], f"Expected first_name {expected['first_name']}, got {actual['first_name']}"
    assert actual["last_name"] == expected["last_name"], f"Expected last_name {expected['last_name']}, got {actual['last_name']}"