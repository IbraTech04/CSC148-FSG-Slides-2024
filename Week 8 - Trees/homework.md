# Week 8 Homework

Here, there are two homework problems. Unfortunately, today's FSG was a bit all over the place so I've provided you with two problems; One that you should be able to solve (at least partially) now, and one that you can attempt, but might not be able to solve until after next week's content.

**1. (The one you can attempt) Lst2Tree:** We know from our knowledge from lecture that nested lists can be used to represent trees. We also know that trees can be represented as nested lists. This is a very powerful concept, and we can use it to convert a nested list into a tree, and vice versa.

Implement the following two methods in the `Tree` class. The first is an initializer that initializes a tree from a nested list. The second is a method that returns the tree's representation as a nested list.

Recall that:

`[1, [2, [3], [4]], [5, [6], [7]]]` is a nested list representation of the following tree:

```
    1
   / \
  2   5
 / \ / \
3  4 6  7
```

```python
class TreeNode:
  """
  Class representing a node in a tree
  """
  # Implementation omitted; Assume it's a standard TreeNode class

    def tree2list(self) -> list[Union[int, list]]:
        """
        Method which creates the nested list representation of the tree
        Precondition: Assume this tree is NOT a cycle
        """
        # TODO: Implement this method
  
def lst2tree(lst: list[Union[int, list]]) -> TreeNode:
    """
    Class method which creates a tree from a nested list
    This method should return the root node of the tree
    Precondition: Assume lst is a valid nested list representation of a tree
    """
    # TODO: Implement this method
```

**2. (The one based on next week; you can still attempt it though!) Chicago Med’s File Problem:** *Dr. Choi* is facing a challenging problem with organizing his medical files. His computer's hard drive contains a complex arrangement of directories and files, forming a *tree-like hierarchical structure.* However, he's noticed that there are numerous duplicate entries scattered throughout this structure, leading to unnecessary clutter and confusion.

To address this issue, Dr. Choi needs assistance in developing a script that will efficiently *remove all duplicate file entries from his directory tree.* Your task is to implement a method that takes the root node of this file system tree as input and eliminates all duplicate file entries, ensuring that each unique file is retained only once. *You can assume the first entry of the file you find is the one to be kept.*

```python
from __future__ import annotations
 
class FileNode:
    """
    Class representing a file in a file system
    
    === Representation Invariants ===
    - file_size >= 0
    len(file_name) > 0
    if default program is None, file_type is also None 
    
    """
    file_name: str
    file_size: float
    file_type: str
    default_program: str
    
    def __init__(self, file_name: str, file_size: float, file_type: str = None, default_program: str = None):
        self.file_name = file_name
        self.file_size = file_size
        self.file_type = file_type
        self.default_program = default_program
    
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, FileNode) and self.file_name == __value.file_name and self.file_size == __value.file_size and self.file_type == __value.file_type and self.default_program == __value.default_program
    
 
class FolderNode:
    """
    Class representing a folder in a file system
    """
    folder_name: str
    folder_size: float
    files: list[FileNode]
    folders: list[FolderNode]
    
    def __init__(self, folder_name: str, folder_size: float, files: list[FileNode] = [], folders: list[FolderNode] = []):
        self.folder_name = folder_name
        self.folder_size = folder_size
        self.files = files
        self.folders = folders
    
    def delete_shortcuts(self) -> None:
        """
        Method which deletes shortcuts/duplicates (Hint: Aliases) of files in the folder recursively
        """
```
