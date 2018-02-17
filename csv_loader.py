# -*- coding: utf-8 -*-

from constants import PROPERTY_ID, PROPERTY_PARENT_ID, \
    PROPERTY_DEPARTMENT_CITY, PROPERTY_DEPARTMENT_NAME, \
    PROPERTY_FIRSTNAME, PROPERTY_SURNAME, PROPERTY_DEPARTMENT_ID, \
    PROPERTY_BIRTHDATE, CSV_TYPE_DEPARTMENT, CSV_TYPE_EMPLOYEE


def load_file(file_name, csv_type):
    result = list()

    with open(file_name, "r") as file:
        for line in file:

            line = line.replace("\n", "")

            if len(line) > 0:
                split_line = line.split(";")
                row = list(map(_replace_empty_cell(), split_line))

                if csv_type == CSV_TYPE_EMPLOYEE:
                    result.append(_employee_csv_file(row))
                if csv_type == CSV_TYPE_DEPARTMENT:
                    result.append(_department_csv_file(row))

    return result


def _replace_empty_cell():
    return lambda x: x if len(x) > 0 else None


def _to_int_or_none():
    return lambda x: int(x) if x else None


def _department_csv_file(row):
    convert = _to_int_or_none()

    return {
        PROPERTY_ID: int(row[0]),
        PROPERTY_PARENT_ID: convert(row[1]),
        PROPERTY_DEPARTMENT_NAME: row[2],
        PROPERTY_DEPARTMENT_CITY: row[3],
    }


def _employee_csv_file(row):
    return {
        PROPERTY_ID: int(row[0]),
        PROPERTY_FIRSTNAME: row[1],
        PROPERTY_SURNAME: row[2],
        PROPERTY_DEPARTMENT_ID: int(row[3]),
        PROPERTY_BIRTHDATE: row[4],
    }
