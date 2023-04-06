from abilities.browse_the_web import BrowseTheWeb
from tasks.task import Task


class NavigateToLogin(Task):

    def __init__(self, base_url):
        self.base_url = base_url

    def perform_as(self, actor):
        ability = actor.ability_to(BrowseTheWeb)
        ability.browser.get(self.base_url)
        # Implement the navigation to the login page using the ability's browser instance
        # Example:
        # ability.browser.get('https://example.com/login')
