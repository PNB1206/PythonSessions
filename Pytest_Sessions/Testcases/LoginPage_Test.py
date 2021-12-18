import pytest
from Pytest_Sessions.PageObjectRepo.Loginpage import logingPage
from Pytest_Sessions.Testcases.Base_test import Base_test


class Test_Login(Base_test):
    def test_searchbox(self):
        self.login = logingPage()
        self.login.enterText_searchbox()