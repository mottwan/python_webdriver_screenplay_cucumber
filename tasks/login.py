from abilities.browse_the_web import BrowseTheWeb
from tasks.task import Task


class Login(Task):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def with_credentials(cls, username, password):
        return cls(username, password)

    def perform_as(self, actor):
        ability = actor.ability_to(BrowseTheWeb)
        # Implement the login process using the ability's browser instance
        # Example:
        # ability.browser.find_element_by_id('username').send_keys(self.username)
        # ability.browser.find_element_by_id('password').send_keys(self.password)
        # ability.browser.find_element_by_id('submit').click()
