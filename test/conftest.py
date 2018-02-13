# -*- coding: utf-8 -*-

import pytest

from data import make_departments_data, make_employees_data


@pytest.fixture(scope="function")
def departments_data():
    yield make_departments_data()


@pytest.fixture(scope="function")
def employees_data():
    yield make_employees_data()
