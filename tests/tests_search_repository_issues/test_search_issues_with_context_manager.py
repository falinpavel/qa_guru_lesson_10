import allure

from helpers.application_manager.application_manager import app


class TestSearchIssues:

    def test_search_issues_with_context_manager(self):
        with allure.step('Open main page'):
            app.page_main_github_unauthorized.open_main_page()
        with allure.step('Search repository and click it'):
            app.page_main_github_unauthorized.search_and_click_repository(repository='falinpavel/qa_guru_lesson_10')
        with allure.step('Open repository issues'):
            app.page_repository.open_repository_issues()
        with allure.step('Check issue title'):
            app.page_repository.check_issue(issue_title='Title for gh pages allure results')
