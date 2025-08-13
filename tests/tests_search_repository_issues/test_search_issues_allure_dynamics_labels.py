import allure

from helpers.application_manager.application_manager import app


class TestSearchIssues:

    def test_search_issues_allure_decorators(self):
        allure.dynamic.epic('Страница репозитория')
        allure.dynamic.feature('Просмотр вкладки "Issues"')
        allure.dynamic.story('Неавторизованный пользовател может просмотреть вкладку "Issues"'
                             ' при поиске репозитория и открыть его для просмотра')
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.issue('https://jira.com/jira-123')
        allure.dynamic.testcase('https://github.com/falinpavel/qa_guru_lesson_10/issues/1')
        allure.dynamic.id(2)
        allure.dynamic.title('Проверка отображения наименования в вкладке "Issues"')
        allure.dynamic.label('owner', 'falinpavel')
        allure.dynamic.description('Проверка "Issues" при поиске репозитория из неавторизованной зоны'
                                   ' и проверка его наименования')
        allure.dynamic.tag('UI Tests')
        app.page_main_github_unauthorized.open_main_page()
        app.page_main_github_unauthorized.search_and_click_repository(repository='falinpavel/qa_guru_lesson_10')
        app.page_repository.open_repository_issues()
        app.page_repository.check_issue(issue_title='Title for gh pages allure results')
