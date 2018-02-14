# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from numpy import mean

from query_language import select_table, where, join, sum
from tree_chart import TreeChart
from data import make_departments_data, make_employees_data
from constants import PROPERTY_ID, PROPERTY_DEPARTMENT_ID, \
    PROPERTY_FIRSTNAME, PROPERTY_SURNAME, PROPERTY_BIRTHDATE


def command1():
    query = where(select_table(make_departments_data()), "ID", 5)

    for i in query:
        print(i)


def command2():
    query = join(make_departments_data(), employees, "ID", "Department-ID")

    for i in query:
        select_columns(i, ("ID", "Firstname"))


def command3():
    tree = TreeChart(node="root")
    created_tree = tree.create_tree()

    t = tree.get_subtree(created_tree, 1)

    query = join([element.node for element in t], make_employees_data(), PROPERTY_ID, PROPERTY_DEPARTMENT_ID)

    for x in query:
        print(x[PROPERTY_FIRSTNAME], x[PROPERTY_SURNAME])


def command4():
    tree = TreeChart(node="root")
    created_tree = tree.create_tree()

    t = tree.get_subtree(created_tree, 1)

    query = join([element.node for element in t], make_employees_data(), PROPERTY_ID, PROPERTY_DEPARTMENT_ID)

    result = list()

    for x in query:
        date_object = datetime.strptime(x[PROPERTY_BIRTHDATE], "%d.%m.%Y")
        result.append(int((datetime.now()-date_object).days/365))

    print(mean(result))


def tree_test():
    tree = TreeChart(node="root")
    created_tree = tree.create_tree()

    t = tree.breadth_fist_walk(created_tree)

    for i in t:
        print(i)


if __name__ == "__main__":
    # command1()
    # command2()
    # command3()
    command4()
    # tree_test()


