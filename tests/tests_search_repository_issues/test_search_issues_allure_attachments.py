import json

import allure
from selene.core import query
from selene.support.shared import browser

from helpers.application_manager.application_manager import app


class TestSearchIssues:

    @allure.epic('Страница репозитория')
    @allure.feature('Просмотр вкладки "Issues"')
    @allure.story('Неавторизованный пользовател может просмотреть вкладку "Issues"'
                  ' при поиске репозитория и открыть его для просмотра')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue('https://jira.com/jira-123')
    @allure.testcase('https://github.com/falinpavel/qa_guru_lesson_10/issues/1')
    @allure.id(3)
    @allure.title('Проверка отображения наименования в вкладке "Issues"')
    @allure.label('owner', 'falinpavel')
    @allure.description('Поиск "Issues" при поиске репозитория из неавторизованной зоны и проверка его наименования')
    @allure.tag('UI Tests')
    def test_search_issues_allure_attachments(self):
        # allure.attach(body=browser.get(query.page_source_saved()), name='Документ page source HTML',
        #               attachment_type=allure.attachment_type.TEXT)
        allure.attach(body='Простой текст', name='Текстовый файл', attachment_type=allure.attachment_type.TEXT)
        # allure.attach(name='Изображение', attachment_type=allure.attachment_type.PNG)
        # allure.attach(name='Документ PDF', attachment_type=allure.attachment_type.PDF)
        # allure.attach(name='Документ XML', attachment_type=allure.attachment_type.XML)
        allure.attach(body=json.dumps({
            "data": {
                "repository": {
                    "search": {
                        "closedIssueCount": 'null',
                        "openIssueCount": 1
                    },
                    "id": "R_kgDOPahsLg"
                }
            }
        }), name='Документ JSON', attachment_type=allure.attachment_type.JSON)
        allure.attach('<h1>Title for gh pages allure results</h1>' ,name='Разметка HTML', attachment_type=allure.attachment_type.HTML)
        app.page_main_github_unauthorized.open_main_page()
        app.page_main_github_unauthorized.search_and_click_repository(repository='falinpavel/qa_guru_lesson_10')
        app.page_repository.open_repository_issues()
        app.page_repository.check_issue(issue_title='Title for gh pages allure results')
