# -*- coding: utf-8 -*-

from tree_chart import TreeChart
from test.conftest import departments_tree


def test_create_tree(departments_tree):
    tree = TreeChart("root")
    create_tree = tree.create_tree(departments_tree)

    whole_tree = tree.tree_to_list_of_dicts(create_tree)

    # whole tree is length + 1 because there is internal
    # 'root' node
    assert 4 == len(whole_tree)


def test_subtree(departments_tree):
    tree = TreeChart("root")
    created_tree = tree.create_tree(departments_tree)

    sub_tree = tree.get_subtree(created_tree, 2)
    assert 2 == len(sub_tree)
