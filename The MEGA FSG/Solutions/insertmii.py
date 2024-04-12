from __future__ import annotations
from typing import Optional


class DLLNode:
    """A node in a linked list."""
    item: any
    _next: Optional[DLLNode]
    _prev: Optional[DLLNode]

    def __init__(self, item: any) -> None:
        self.item = item
        self._next = None
        self._prev = None

class DoublyLinkedList:
    """A doubly linked list."""
    _first: Optional[DLLNode]
    _last: Optional[DLLNode]

    def __init__(self, lst) -> None:
        if len(lst) == 0:
            self._first = self._last = None
        else:
            self._first = DLLNode(lst[0])
            current = self._first
            for item in lst[1:]:
                new_node = DLLNode(item)
                current._next = new_node
                new_node._prev = current
                current = new_node
            self._last = current
    
    def __str__(self) -> str:
        current = self._first
        result = ''
        while current is not None:
            result += str(current.item) + ' '
            current = current._next
        
        current_rev = self._last
        result_rev = ''
        while current_rev is not None:
            result_rev += str(current_rev.item) + ' '
            current_rev = current_rev._prev
        assert result.strip() == result_rev[::-1].strip() # This line is here to make sure you reconstructed the pointers correctly in both directions.
        return result.strip()

    def insert_last_1(self, value: any, after: any) -> bool:
        """
        >>> sl = DoublyLinkedList([7, 2, 7, 3])
        >>> str(sl) 
        '7 2 7 3'
        >>> sl.insert_last_1(5, 7)
        True
        >>> str(sl)
        '7 2 7 5 3'
        >>> sl.insert_last_1(9, 8)
        False
        >>> str(sl)
        '7 2 7 5 3'
        """
        if self._last is None: # If the list is empty, we return False.
            return False
        current = self._last
        while current is not None:
            if current.item == after: # If we find the node we're looking for, we insert the new node after it.
                new_node = DLLNode(value)
                new_node._prev = current
                new_node._next = current._next
                if current._next is not None:
                    current._next._prev = new_node
                current._next = new_node
                if current == self._last: # If the node we're looking for is the last node, we update the last pointer.
                    self._last = new_node
                return True
            current = current._prev
        return False # If we reach the beginning of the list without finding the node, we return False.

    def insert_last_2(self, value: any, after: any) -> bool:
        """
        >>> sl = DoublyLinkedList([7, 2, 7, 3])
        >>> str(sl) 
        '7 2 7 3'
        >>> sl.insert_last_2(5, 7)
        True
        >>> str(sl)
        '7 2 7 5 3'
        >>> sl.insert_last_2(9, 8)
        False
        >>> str(sl)
        '7 2 7 5 3'
        """
        if self._first is None: # If the list is empty, we return False.
            return False
        current = self._first
        last_occurrence = None
        while current is not None:
            if current.item == after: # If we find the node we're looking for, we update the last occurrence pointer.
                last_occurrence = current
            current = current._next
        if last_occurrence is None: # If we don't find the node, we return False.
            return False
        new_node = DLLNode(value) # Otherwise, we insert the new node after the last occurrence of the node.
        new_node._prev = last_occurrence
        new_node._next = last_occurrence._next
        if last_occurrence._next is not None:
            last_occurrence._next._prev = new_node
        last_occurrence._next = new_node
        if last_occurrence == self._last: # If the last occurrence is the last node, we update the last pointer.
            self._last = new_node
        return True

if __name__ == '__main__':
    # Test the implementation
    import doctest
    doctest.testmod()