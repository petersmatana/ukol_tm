# -*- coding: utf-8 -*-

from itertools import *

from data import make_departments_data, make_employees_data

departments = make_departments_data()
employees = make_employees_data()


def get_department():
    for department in departments:
        yield department


def where(structure, column, value):
    for entity in structure:
        if entity[column] == value:
            yield entity


def join(structure_1, structure_2, structure_1_key, structure_2_key):
    for entity_1 in structure_1:
        for entity_2 in structure_2:
            if entity_1[structure_1_key] == entity_2[structure_2_key]:
                yield dict(list(entity_1.items()) + list(entity_2.items()))


def select_columns(entity, colums):
    for key, value in entity.items():
        if key in colums:
            print("key = {} , value = {}".format(key, value))


def command1():
    query = where(get_department(), "ID", 5)

    for i in query:
        print(i)


def command2():
    query = join(departments, employees, "ID", "Department-ID")

    for i in query:
        select_columns(i, ("ID", "Firstname"))
