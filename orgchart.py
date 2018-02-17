# -*- coding: utf-8 -*-

import pprint
from datetime import datetime, timedelta
from numpy import mean, sum
from sys import stdin, argv

from constants import PROPERTY_ID, PROPERTY_DEPARTMENT_ID, \
    PROPERTY_FIRSTNAME, PROPERTY_SURNAME, PROPERTY_BIRTHDATE, \
    PROPERTY_DEPARTMENT_NAME, PROPERTY_DEPARTMENT_CITY, \
    CSV_TYPE_DEPARTMENT, CSV_TYPE_EMPLOYEE
from csv_loader import load_file
from query_language import select_table, where, join, sum, \
    select_columns
from test.data import make_departments_data, make_employees_data
from tree_chart import TreeChart


def command1(department, department_id):
    """
    Get department name and city for department ID.

    example input: Department 42

    :param department_id: Department ID
    """

    query = where(select_table(department), "ID", department_id)

    for i in query:
        print("{}, {}".format(i[PROPERTY_DEPARTMENT_NAME], i[PROPERTY_DEPARTMENT_CITY]))


def command2(department, employee, department_id):
    """
    Get number of employees in department. It is whole department and it's
    sub-departments.

    example input: Count 13

    :param department_id: Department ID
    """

    tree = TreeChart(node="root")
    created_tree = tree.create_tree(department)

    t = tree.get_subtree(created_tree, department_id)

    query = sum(join([element.node for element in t], employee, "ID", "Department-ID"))

    print(query)


def command3(department, employee, department_id):
    """
    Get firstname and surname for employees in department and it's
    sub-departments.

    example input: People 7

    :param department_id: Department ID
    """

    tree = TreeChart(node="root")
    created_tree = tree.create_tree(department)

    t = tree.get_subtree(created_tree, department_id)

    query = join([element.node for element in t], employee,
                 PROPERTY_ID, PROPERTY_DEPARTMENT_ID)

    for x in query:
        print(x[PROPERTY_FIRSTNAME], x[PROPERTY_SURNAME])


def command4(department, employee, department_id):
    """
    Get average of age for employees in department and it's
    sub-departments.

    example input: Average 3

    :param department_id: Department ID
    """

    tree = TreeChart(node="root")
    created_tree = tree.create_tree(department)

    t = tree.get_subtree(created_tree, department_id)

    query = join([element.node for element in t], employee,
                 PROPERTY_ID, PROPERTY_DEPARTMENT_ID)

    result = list()

    for x in query:
        date_object = datetime.strptime(x[PROPERTY_BIRTHDATE], "%d.%m.%Y")
        result.append(int((datetime.now()-date_object).days/365))

    if len(result) > 0:
        print(mean(result))
    else:
        print("0")


def user_input(department, employee):
    print("your command: ")

    while 1:
        try:
            line = stdin.readline()
        except KeyboardInterrupt:
            break
        if not line:
            break

        print("your command: ")
        split = line.split(" ")

        if split[0] == "Department":
            command1(department, int(split[1]))
            continue
        if split[0] == "Count":
            command2(department, employee, int(split[1]))
            continue
        if split[0] == "People":
            command3(department, employee, int(split[1]))
            continue
        if split[0] == "Average":
            command4(department, employee, int(split[1]))
            continue
        print("bad command")


def process_csv_files():
    if len(argv) != 3:
        print("need csv file with departments and employees")

    department = load_file(argv[1], CSV_TYPE_DEPARTMENT)
    employee = load_file(argv[2], CSV_TYPE_EMPLOYEE)

    return department, employee


def test():
    department, employee = process_csv_files()

    pp = pprint.PrettyPrinter(indent=3)
    pp.pprint(department)
    pp.pprint(employee)

    command1(department, 1)
    command2(department, employee, 1)
    command3(department, employee, 1)
    command4(department, employee, 1)


# python orgchart.py /home/smonty/Downloads/orgchart-data.csv /home/smonty/Downloads/employees-data.csv
if __name__ == "__main__":
    # test()

    department, employee = process_csv_files()

    user_input(department, employee)
