from behave import when, then
from utils.api_helper import APIClient

@when('user send a GET request to "{endpoint}"')
def execute_endpoint(context, endpoint):
    if not hasattr(context, "api_client"):
        context.api_client = APIClient()
    context.response = context.api_client.get(endpoint)
    context.response_json = context.response.json()

@then('the response code should be {status_code:d}')
def verify_status(context, status_code):
    assert context.response.status == status_code, f"Expected {status_code}, got {context.response.status}"

@then('the user details should be present:')
def verify_data(context):
    expected = context.table[0]
    actual = context.response_json["data"]
    assert actual["email"] == expected["email"]
    assert actual["first_name"] == expected["first_name"]
    assert actual["last_name"] == expected["last_name"]