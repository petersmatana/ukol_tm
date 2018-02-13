# -*- coding: utf-8 -*-

from query_language import select_table, where
from data import make_departments_data, make_employees_data


def test_select_table_all_departments(departments_data):
    assert len(make_departments_data()) == len(departments_data)


def test_select_table_all_employees(employees_data):
    assert len(make_employees_data()) == len(employees_data)


def test_where_departments(departments_data):
    column = "ID"
    value = 1

    query = where(select_table(departments_data), column, value)

    for department in make_departments_data():
        if department[column] == value:
            for element in query:
                assert department == element


def test_where_employees(employees_data):
    column = "Firstname"
    value = "Jan"

    query = where(select_table(employees_data), column, value)

    for employee in make_employees_data():
        if employee[column] == value:
            for element in query:
                assert employee == element
