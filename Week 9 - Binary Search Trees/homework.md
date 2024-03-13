# Week 9 Homework

Only one homework question this time around; It's a bit more tricky than last week, and has 3 parts. So I think it's a fair compromise.

**1. Lst2TreeV2:** The following questions are based all around tree traversals, and what you can do with them. You'll be implementing a few methods, and answering some theory-based questions as well

### Part A: Postorder Traversal
We know from our knowledge from the FSG that given an arbitrary tree's (not necissarily a BST) preorder and postorder traversal, we **cannot** reconstruct the same original tree. However, the same does not hold true for BSTs. 

Implement the following method which takes in a list of integers (representing the postorder traversal of a BST) and returns the root node of the tree.

```python
def postorder2bst(postorder: list[int]) -> TreeNode:
    """
    Class method which creates a BST from a postorder traversal
    This method should return the root node of the tree
    Precondition: Assume postorder is a valid postorder traversal of a BST
    Challenge! Can you implement this method without the precondition? That is, implement your own error checking for the postorder traversal
    """
    # TODO: Implement this method
```

### Part B: Preorder Traversal
We know we can reconstruct a tree from its postorder traversal, but can we do the same with its preorder traversal? Why or why not? If so, implement the following method which takes in a list of integers (representing the preorder traversal of a BST) and returns the root node of the tree.

```python
def preorder2bst(preorder: list[int]) -> TreeNode:
    """
    Class method which creates a BST from a preorder traversal
    This method should return the root node of the tree
    Precondition: Assume preorder is a valid preorder traversal of a BST
    Challenge! Can you implement this method without the precondition? That is, implement your own error checking for the preorder traversal
    """
```

### Part C: Inorder Traversal
Does the same hold true for the in-order traversal? Why or why not?

*Hint: Recall our example of AVL Trees, specifically the video showing insertions and rotations. What did you notice about the in-order traversal before and after each rotation?*