# -*- coding: utf-8 -*-

import pytest

from constants import PROPERTY_ID, PROPERTY_PARENT_ID, \
    PROPERTY_DEPARTMENT_NAME, PROPERTY_DEPARTMENT_CITY
from test.data import make_departments_data, make_employees_data


@pytest.fixture(scope="function")
def departments_data():
    yield make_departments_data()


@pytest.fixture(scope="function")
def employees_data():
    yield make_employees_data()


@pytest.fixture(scope="function")
def departments_tree():
    d1 = {
        PROPERTY_ID: 1,
        PROPERTY_PARENT_ID: None,
        PROPERTY_DEPARTMENT_NAME: "d1",
        PROPERTY_DEPARTMENT_CITY: "c1",
    }

    d2 = {
        PROPERTY_ID: 2,
        PROPERTY_PARENT_ID: 1,
        PROPERTY_DEPARTMENT_NAME: "d2",
        PROPERTY_DEPARTMENT_CITY: "c2",
    }

    d3 = {
        PROPERTY_ID: 3,
        PROPERTY_PARENT_ID: 2,
        PROPERTY_DEPARTMENT_NAME: "d3",
        PROPERTY_DEPARTMENT_CITY: "c3",
    }

    yield d1, d2, d3
