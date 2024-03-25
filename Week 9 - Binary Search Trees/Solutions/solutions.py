from __future__ import annotations
from typing import Any, Optional

class BinarySearchTree:
    """Binary Search Tree class.

    This class represents a binary tree satisfying the Binary Search Tree
    property: for every node, its value is >= all items stored in its left
    subtree, and <= all items stored in its right subtree.
    """
    # === Private Attributes ===
    # The item stored at the root of the tree, or None if the tree is empty.
    _root: Optional[Any]
    # The left subtree, or None if the tree is empty.
    _left: Optional[BinarySearchTree]
    # The right subtree, or None if the tree is empty.
    _right: Optional[BinarySearchTree]
    
    
    def __init__(self, root: Optional[Any]) -> None:
        """Initialize a new BST containing only the given root value.

        If <root> is None, initialize an empty BST.
        """
        if root is None:
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinarySearchTree(None)   # self._left is an empty BST
            self._right = BinarySearchTree(None)  # self._right is an empty BST

    def is_empty(self) -> bool:
        """Return whether this BST is empty.
        """
        return self._root is None

    def insert(self, item: Any) -> None:
        """Insert <item> into this BST, maintaining the BST property.
        """
        if self.is_empty():
            self._root = item
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)
        elif item < self._root:
            self._left.insert(item)
        elif item > self._root:
            self._right.insert(item)

    def __str__(self) -> str:
        """Return a string representation of this tree."""
        return self._str_helper(self, 0)

    def _str_helper(self, node: BinarySearchTree, level: int) -> str:
        """Helper method for __str__ to recursively build the string representation of the tree."""
        if node.is_empty():
            return ''
        else:
            tree_str = ''
            tree_str += self._str_helper(node._right, level + 1)
            tree_str += '  ' * level + str(node._root) + '\n'
            tree_str += self._str_helper(node._left, level + 1)
            return tree_str

    def __eq__(self, other: Any) -> bool:
        """Return whether this BST is equal to the other BST.
        """
        if isinstance(other, BinarySearchTree):
            return self._root == other._root and self._left == other._left and self._right == other._right
        return False

    def preorder(self) -> list:
        """Return a list of this tree's items using a pre-order traversal.
        """
        if self.is_empty():
            return []
        else:
            return [self._root] + self._left.preorder() + self._right.preorder()
    
    def postorder(self) -> list:
        """Return a list of this tree's items using a post-order traversal.
        """
        if self.is_empty():
            return []
        else:
            return self._left.postorder() + self._right.postorder() + [self._root]


def reconstruct_from_postorder(lst: list[int]) -> BinarySearchTree:
    """Return the BinarySearchTree that is reconstructed from the given
    postorder traversal <lst>.
    """
    if len(lst) == 0:
        return BinarySearchTree(None)
    else:
        root = lst[-1]
        left_lst = []
        right_lst = []
        for i in range(len(lst) - 1):
            if lst[i] < root:
                left_lst.append(lst[i])
            else:
                right_lst.append(lst[i])
        left_tree = reconstruct_from_postorder(left_lst)
        right_tree = reconstruct_from_postorder(right_lst)
        new_tree = BinarySearchTree(root)
        new_tree._left = left_tree
        new_tree._right = right_tree
        return new_tree

def reconstruct_from_preorder(lst: list[int]) -> BinarySearchTree:
    """Return the BinarySearchTree that is reconstructed from the given
    preorder traversal <lst>.
    """
    if len(lst) == 0:
        return BinarySearchTree(None)
    else:
        root = lst[0]
        left_lst = []
        right_lst = []
        for i in range(1, len(lst)):
            if lst[i] < root:
                left_lst.append(lst[i])
            else:
                right_lst.append(lst[i])
        left_tree = reconstruct_from_preorder(left_lst)
        right_tree = reconstruct_from_preorder(right_lst)
        new_tree = BinarySearchTree(root)
        new_tree._left = left_tree
        new_tree._right = right_tree
        return new_tree
