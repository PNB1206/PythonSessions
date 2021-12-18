import pytest

from Pytest_Sessions.Testcases.conftest import init_driver


@pytest.mark.usefixtures('init_driver')
class Base_test:
    pass