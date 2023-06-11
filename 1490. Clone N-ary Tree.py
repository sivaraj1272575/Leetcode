"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        new_child = Node(root.val, [])
        for i in root.children:
            new_child.children.append(self.cloneTree(i))
        return new_child
