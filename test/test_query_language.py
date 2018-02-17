# -*- coding: utf-8 -*-

from query_language import select_table, where, join
from test.data import make_departments_data, make_employees_data
from constants import PROPERTY_ID, PROPERTY_FIRSTNAME, PROPERTY_DEPARTMENT_ID


def test_select_table_all_departments(departments_data):
    assert len(make_departments_data()) == len(departments_data)


def test_select_table_all_employees(employees_data):
    assert len(make_employees_data()) == len(employees_data)


def test_where_departments(departments_data):
    column = PROPERTY_ID
    value = 1

    query = where(select_table(departments_data), column, value)

    for department in make_departments_data():
        if department[column] == value:
            for element in query:
                assert department == element


def test_where_employees(employees_data):
    column = PROPERTY_FIRSTNAME
    value = "Jan"

    query = where(select_table(employees_data), column, value)

    for employee in make_employees_data():
        if employee[column] == value:
            for element in query:
                assert employee == element


def test_join(departments_data, employees_data):
    query = join(departments_data, employees_data,
                 PROPERTY_ID, PROPERTY_DEPARTMENT_ID)

    count = 0
    for _ in query:
        count += 1

    assert 3 == count
