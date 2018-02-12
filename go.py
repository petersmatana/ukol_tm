# -*- coding: utf-8 -*-

from data import make_departments_data

departments = make_departments_data()


def get_department():
    for department in departments:
        yield department


def get_by(structure, column_name):
    for entity in structure:
        yield entity[column_name]


def go():
    query = get_by(get_department(), "DepartmentName")

    for i in query:
        print(i)
