**Chicago Med’s File Problem:** *Dr. Choi* is facing a challenging problem with organizing his medical files. His computer's hard drive contains a complex arrangement of directories and files, forming a *tree-like hierarchical structure.* However, he's noticed that there are numerous duplicate entries scattered throughout this structure, leading to unnecessary clutter and confusion.

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