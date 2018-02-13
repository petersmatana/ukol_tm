# -*- coding: utf-8 -*-

from query_language import select_table, where, join, sum
from tree_chart import TreeChart
from data import make_departments_data, make_employees_data
from constants import PROPERTY_ID, PROPERTY_DEPARTMENT_ID


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

    for i in t:
        print(i)

    # print(query)


def tree_test():
    tree = TreeChart(node="root")
    created_tree = tree.create_tree()

    t = tree.breadth_fist_walk(created_tree)

    for i in t:
        print(i)


if __name__ == "__main__":
    # command1()
    # command2()
    command3()
    # tree_test()


