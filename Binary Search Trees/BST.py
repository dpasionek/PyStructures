from typing import Any


class Node(object):
    def __init__(self, value = None) -> None:
        self.value: Any = value
        self.right_child = None 
        self.left_child = None

class BST(object):
    def __init__(self, root: Node) -> None:
        self.root = root
        self.height = 0

    def Insert(self, node: Node) -> None:
        parentNode = self.Search(node.value, captureParent=True)
        print(f"Node: {node.value}   Parent Node {parentNode.value}")
        if(node.value >= parentNode.value):
            parentNode.right_child = node
        else:
            parentNode.left_child = node
        self.PrintTree(self.root)
        print("------------------------")

    def Delete(self, node_value: Any) -> None:
        pass

    def Search(self, node_value: Any, captureParent = False) -> Node:
        search_node = self.root
        prev_node = None
        while(search_node != None and (captureParent or search_node.value != node_value)):
            if(node_value >= search_node.value): # Move Right
                prev_node = search_node
                search_node = search_node.right_child
            else: # Move Left
                prev_node = search_node
                search_node = search_node.left_child
        return search_node if captureParent is not True else prev_node

    def PrintTree(self, node, level = 0):
        if node != None:
            self.PrintTree(node.right_child, level + 1)
            print(' ' * 5 * level + '-> ' + str(node.value))
            self.PrintTree(node.left_child, level + 1)
node = Node(5)
node.left_child = Node(4)
node.right_child = Node(6)

tree = BST(node)
tree.Insert(Node(5))
tree.Insert(Node(5))
tree.Insert(Node(4))
tree.Insert(Node(3))
tree.Insert(Node(2))
tree.Insert(Node(1))

