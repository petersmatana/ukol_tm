# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from numpy import mean, sum
from sys import stdin

from query_language import select_table, where, join, sum, \
    select_columns
from tree_chart import TreeChart
from data import make_departments_data, make_employees_data
from constants import PROPERTY_ID, PROPERTY_DEPARTMENT_ID, \
    PROPERTY_FIRSTNAME, PROPERTY_SURNAME, PROPERTY_BIRTHDATE, \
    PROPERTY_DEPARTMENT_NAME, PROPERTY_DEPARTMENT_CITY


def command1(department_id):
    """
    Get department name and city for department ID.

    example input: Department 42

    :param department_id: Department ID
    """

    query = where(select_table(make_departments_data()), "ID", department_id)

    for i in query:
        print("{}, {}".format(i[PROPERTY_DEPARTMENT_NAME], i[PROPERTY_DEPARTMENT_CITY]))


def command2(department_id):
    """
    Get number of employees in department. It is whole department and it's
    sub-departments.

    example input: Count 13

    :param department_id: Department ID
    """

    tree = TreeChart(node="root")
    created_tree = tree.create_tree()

    t = tree.get_subtree(created_tree, department_id)

    query = join([element.node for element in t], make_employees_data(), "ID", "Department-ID")

    count = 0
    for _ in query:
        count += 1

    print(count)


def command3(department_id):
    """
    Get firstname and surname for employees in department and it's
    sub-departments.

    example input: People 7

    :param department_id: Department ID
    """

    tree = TreeChart(node="root")
    created_tree = tree.create_tree()

    t = tree.get_subtree(created_tree, department_id)

    query = join([element.node for element in t], make_employees_data(),
                 PROPERTY_ID, PROPERTY_DEPARTMENT_ID)

    for x in query:
        print(x[PROPERTY_FIRSTNAME], x[PROPERTY_SURNAME])


def command4(department_id):
    """
    Get average of age for employees in department and it's
    sub-departments.

    example input: Average 3

    :param department_id: Department ID
    """

    tree = TreeChart(node="root")
    created_tree = tree.create_tree()

    t = tree.get_subtree(created_tree, department_id)

    query = join([element.node for element in t], make_employees_data(),
                 PROPERTY_ID, PROPERTY_DEPARTMENT_ID)

    result = list()

    for x in query:
        date_object = datetime.strptime(x[PROPERTY_BIRTHDATE], "%d.%m.%Y")
        result.append(int((datetime.now()-date_object).days/365))

    if len(result) > 0:
        print(mean(result))
    else:
        print("0")


def user_input():
    while 1:
        try:
            line = stdin.readline()
        except KeyboardInterrupt:
            break
        if not line:
            break

        split = line.split(" ")

        if split[0] == "Department":
            command1(int(split[1]))
            continue
        if split[0] == "Count":
            command2(int(split[1]))
            continue
        if split[0] == "People":
            command3(int(split[1]))
            continue
        if split[0] == "Average":
            command4(int(split[1]))
            continue
        print("bad command")


if __name__ == "__main__":
    user_input()
