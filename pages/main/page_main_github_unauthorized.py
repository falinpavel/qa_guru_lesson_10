from selene.support.shared import browser
from selene.support import by


class MainPageGithub:

    URL = 'https://github.com/'

    def open_main_page(self) -> 'MainPageGithub':
        browser.open(self.URL)
        return self

    def search_and_click_repository(self, repository) -> 'MainPageGithub':
        browser.element('.search-input').click()
        browser.element('#query-builder-test').click().type(repository).press_enter()
        browser.element(by.link_text(repository)).click()
        return self
