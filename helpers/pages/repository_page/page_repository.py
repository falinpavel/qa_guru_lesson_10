import allure
from selene import be, have
from selene.support.shared import browser
from selene.support import by


class RepositoryPage:

    URL = '/falinpavel/qa_guru_lesson_10'

    @allure.step('Open repository page')
    def open_repository_page(self):
        browser.open(self.URL)
        return self

    @allure.step('Open repository issues')
    def open_repository_issues(self):
        browser.element("#issues-tab").click()
        return self

    @allure.step('Check issue title')
    def check_issue(self, issue_title: str):
        browser.element('[data-testid="issue-pr-title-link"]').should(have.exact_text(issue_title))
        return self
