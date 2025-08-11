import allure

from helpers.application_manager.application_manager import app


class TestSearchIssues:

    @allure.epic('Страница репозитория')
    @allure.feature('Просмотр вкладки "Issues"')
    @allure.story('Неавторизованный пользовател может просмотреть вкладку "Issues"'
                  ' при поиске репозитория и открыть его для просмотра')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue('https://jira.com/jira-123')
    @allure.testcase('https://github.com/falinpavel/qa_guru_lesson_10/issues/1')
    @allure.id(1)
    @allure.title('Проверка отображения наименования в вкладке "Issues"')
    @allure.label('owner', 'falinpavel')
    @allure.description('Поиск "Issues" при поиске репозитория из неавторизованной зоны и проверка его наименования')
    @allure.tag('UI Tests')
    def test_search_issues(self):
        with allure.step('Open main page'):
            app.page_main_github_unauthorized.open_main_page()
        with allure.step('Search repository and click it'):
            app.page_main_github_unauthorized.search_and_click_repository(repository='falinpavel/qa_guru_lesson_10')
        with allure.step('Open repository issues'):
            app.page_repository.open_repository_issues()
        with allure.step('Check issue title'):
            app.page_repository.check_issue(issue_title='Title for gh pages allure results')
