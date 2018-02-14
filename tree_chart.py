# -*- coding: utf-8 -*-

from query_language import select_table, departments
from constants import PROPERTY_ID, PROPERTY_PARENT_ID


class TreeChart(object):

    def __init__(self, node):
        self.child_nodes = list()
        self.node = node
        # self.department = department
        self.tree_result = list()

    def __str__(self):
        return str(self.node)

    def add_child_node(self, child_node):
        self.child_nodes.append(child_node)

    def _insert_into_tree(self, root, element):
        for tmp in root.child_nodes:
            if tmp.node[PROPERTY_ID] == element.node[PROPERTY_PARENT_ID]:
                tmp.add_child_node(element)
            else:
                self._insert_into_tree(tmp, element)

    def create_tree(self):
        root = TreeChart("root")

        query = select_table(departments)

        for element in query:
            tree = TreeChart(element)
            if not element[PROPERTY_PARENT_ID]:
                root.add_child_node(tree)
            else:
                self._insert_into_tree(root, tree)

        return root

    def breadth_fist_walk(self, node):
        # print("node = ", node)
        # yield node
        self.tree_result.append(node)
        for element in node.child_nodes:
            self.breadth_fist_walk(element)
        return self.tree_result

    def get_subtree(self, root, department_id):
        for element in root.child_nodes:
            if element.node[PROPERTY_ID] == department_id:
                self.breadth_fist_walk(element)
            else:
                self.get_subtree(element, department_id)
        return self.tree_result

    def tree_to_list_of_dicts(self, tree):
        result = list()
        for element in self.breadth_fist_walk(tree):
            result.append(element.node)

        return result
