from abilities.browse_the_web import BrowseTheWeb
from questions.question import Question


class IsUserLoggedIn(Question):
    def answered_by(self, actor):
        ability = actor.ability_to(BrowseTheWeb)
        # Implement the check for user's logged-in state using the ability's browser instance
        # Example:
        # dashboard_element = ability.browser.find_element_by_id('dashboard')
        # return dashboard_element is not None
        return ability
