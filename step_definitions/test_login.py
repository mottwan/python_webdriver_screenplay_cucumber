import os
import allure
from dotenv import load_dotenv
from pytest_bdd import scenarios, given, when, then

from questions.see_the_dashboard import SeeTheDashboard
from tasks.navigate_to_login import NavigateToLogin as navigate_to_login
from tasks.login import Login as login
from outcomes.common_outcomes import assert_equal

load_dotenv()

base_url = os.environ['BASE_URL']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']


scenarios('../features/login.feature')


@given('the user is on the login page')
@allure.step('The user is on the login page')
def user_on_login_page(actor):
    actor.attempts_to(navigate_to_login(base_url))


@when('the user logs in with valid credentials')
@allure.step('The user logs in with valid credentials')
def user_logs_in(actor):
    actor.attempts_to(
        navigate_to_login(base_url),
        login.with_credentials(username, password),
    )


@then('the user should see the dashboard')
@allure.step('The user should see the dashboard')
def user_sees_dashboard(actor):
    dashboard_visible = actor.should(SeeTheDashboard())
    assert_equal(dashboard_visible, True, "The user should see the dashboard")
