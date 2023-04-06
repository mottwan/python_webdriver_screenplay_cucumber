from abilities.ability import Ability


class BrowseTheWeb(Ability):
    def __init__(self, browser):
        self.browser = browser

    @classmethod
    def using(cls, browser):
        return cls(browser)
