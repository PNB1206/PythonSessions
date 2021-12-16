import pytest
from Pytest_Sessions.PageObjectRepo.Loginpage import logingPage


class Test_Login:
    def test_searchbox(self):
        self.login = logingPage()
        self.login.enterText_searchbox()