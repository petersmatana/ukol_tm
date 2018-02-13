# -*- coding: utf-8 -*-

from tree_chart import TreeChart
from test.conftest import departments_tree


def test_create_tree(departments_tree):
    tree = TreeChart("root")
    create_tree = tree.create_tree()
    tree.breadth_fist_walk(create_tree)
    assert 3 == \
           len(departments_tree)
