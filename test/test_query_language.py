# -*- coding: utf-8 -*-

from query_language import select_table, where
from data import make_departments_data


def test_select_table_all_departments(departments_data):
    assert 9 == len(departments_data)


def test_select_table_all_employees(employees_data):
    assert 2 == len(employees_data)


def test_where_departments(departments_data):
    query = where(select_table(departments_data), "ID", 1)

    for department in make_departments_data():
        if department["ID"] == 1:
            for element in query:
                assert department == element
