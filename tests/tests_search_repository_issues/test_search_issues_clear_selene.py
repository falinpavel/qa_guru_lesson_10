import allure

from helpers.application_manager.application_manager import app


class TestSearchIssues:

    def test_search_issues_clear_selene(self):
        app.page_main_github_unauthorized.open_main_page()
        app.page_main_github_unauthorized.search_and_click_repository(repository='falinpavel/qa_guru_lesson_10')
        app.page_repository.open_repository_issues()
        app.page_repository.check_issue(issue_title='Title for gh pages allure results')
