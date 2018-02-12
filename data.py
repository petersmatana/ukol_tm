# -*- coding: utf-8 -*-


def make_departments_data():
    d1 = {"ID": 1, "Parent-ID": None, "DepartmentName": "Delivery", "DepartmentCity": "Brno"}
    d2 = {"ID": 2, "Parent-ID": None, "DepartmentName": "Support", "DepartmentCity": "Brno"}
    d3 = {"ID": 3, "Parent-ID": None, "DepartmentName": "Marketing", "DepartmentCity": "Praha"}
    d4 = {"ID": 4, "Parent-ID": None, "DepartmentName": "Backoffice", "DepartmentCity": "Praha"}
    d5 = {"ID": 5, "Parent-ID": 1, "DepartmentName": "Testing", "DepartmentCity": "Praha"}
    d6 = {"ID": 6, "Parent-ID": 1, "DepartmentName": "Development", "DepartmentCity": "Brno"}
    d7 = {"ID": 7, "Parent-ID": 6, "DepartmentName": "Python", "DepartmentCity": "Brno"}
    d8 = {"ID": 8, "Parent-ID": 6, "DepartmentName": "Java", "DepartmentCity": "Brno"}

    return d1, d2, d3, d4, d4, d5, d6, d7, d8
