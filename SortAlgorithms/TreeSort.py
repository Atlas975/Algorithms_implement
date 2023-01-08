from dataclasses import dataclass
import random
from typing import optional
from numpy import double


@dataclass
class TreeNode:
    value: double
    left: TreeNode = None
    right: TreeNode = None


# def tree_sort(data):
#     root =
#     for i in data:
#         root
#     pass

# def sort(data):
#     root=None
#     for i in data:
#         root=insert(root,i)


def inorder(tree, res):
    if tree == None:
        return
    inorder(tree.left, res)
    res.append(tree.value)
    inorder(tree.right, res)


def insert(node, value):
    if node == None:
        return TreeNode(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


data = random.sample(range(1000), 10)
print(f"Dataset: {data}")


print(f"Insertion sort: {tree_sort(data)}")
