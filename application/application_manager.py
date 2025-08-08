from pages.main.page_main_github_unauthorized import MainPageGithub
from pages.repository_page.page_repository import RepositoryPage


class ApplicationManager:

    def __init__(self):
        self.page_main_github_unauthorized = MainPageGithub()
        self.page_repository = RepositoryPage()


app = ApplicationManager()
