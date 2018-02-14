# -*- coding: utf-8 -*-

from constants import PROPERTY_ID, PROPERTY_PARENT_ID, \
    PROPERTY_DEPARTMENT_NAME, PROPERTY_DEPARTMENT_CITY, \
    PROPERTY_FIRSTNAME, PROPERTY_SURNAME, PROPERTY_BIRTHDATE, \
    PROPERTY_DEPARTMENT_ID


def make_departments_data():
    d1 = {
        PROPERTY_ID: 1,
        PROPERTY_PARENT_ID: None,
        PROPERTY_DEPARTMENT_NAME: "Delivery",
        PROPERTY_DEPARTMENT_CITY: "Brno",
    }

    d2 = {
        PROPERTY_ID: 2,
        PROPERTY_PARENT_ID: None,
        PROPERTY_DEPARTMENT_NAME: "Support",
        PROPERTY_DEPARTMENT_CITY: "Brno",
    }

    d3 = {
        PROPERTY_ID: 3,
        PROPERTY_PARENT_ID: None,
        PROPERTY_DEPARTMENT_NAME: "Marketing",
        PROPERTY_DEPARTMENT_CITY: "Praha",
    }

    d4 = {
        PROPERTY_ID: 4,
        PROPERTY_PARENT_ID: None,
        PROPERTY_DEPARTMENT_NAME: "Backoffice",
        PROPERTY_DEPARTMENT_CITY: "Praha",
    }

    d5 = {
        PROPERTY_ID: 5,
        PROPERTY_PARENT_ID: 1,
        PROPERTY_DEPARTMENT_NAME: "Testing",
        PROPERTY_DEPARTMENT_CITY: "Praha",
    }

    d6 = {
        PROPERTY_ID: 6,
        PROPERTY_PARENT_ID: 1,
        PROPERTY_DEPARTMENT_NAME: "Development",
        PROPERTY_DEPARTMENT_CITY: "Brno",
    }

    d7 = {
        PROPERTY_ID: 7,
        PROPERTY_PARENT_ID: 6,
        PROPERTY_DEPARTMENT_NAME: "Python",
        PROPERTY_DEPARTMENT_CITY: "Brno",
    }

    d8 = {
        PROPERTY_ID: 8,
        PROPERTY_PARENT_ID: 6,
        PROPERTY_DEPARTMENT_NAME: "Java",
        PROPERTY_DEPARTMENT_CITY: "Brno",
    }

    d9 = {
        PROPERTY_ID: 9,
        PROPERTY_PARENT_ID: 8,
        PROPERTY_DEPARTMENT_NAME: "Java QA",
        PROPERTY_DEPARTMENT_CITY: "Brno",
    }

    d10 = {
        PROPERTY_ID: 10,
        PROPERTY_PARENT_ID: 8,
        PROPERTY_DEPARTMENT_NAME: "Java dev",
        PROPERTY_DEPARTMENT_CITY: "Brno",
    }

    return d1, d2, d3, d4, d5, d6, d7, d8, d9, d10


def make_employees_data():
    e1 = {
        PROPERTY_ID: 1,
        PROPERTY_FIRSTNAME: "Jan",
        PROPERTY_SURNAME: "Hora",
        PROPERTY_DEPARTMENT_ID: 7,
        PROPERTY_BIRTHDATE: "12.03.1994",
    }

    e2 = {
        PROPERTY_ID: 2,
        PROPERTY_FIRSTNAME: "Jiří",
        PROPERTY_SURNAME: "Vereš",
        PROPERTY_DEPARTMENT_ID: 5,
        PROPERTY_BIRTHDATE: "20.08.1986",
    }

    e3 = {
        PROPERTY_ID: 3,
        PROPERTY_FIRSTNAME: "Supp",
        PROPERTY_SURNAME: "Ort",
        PROPERTY_DEPARTMENT_ID: 2,
        PROPERTY_BIRTHDATE: "01.01.1970",
    }

    return e1, e2, e3
