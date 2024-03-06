# Solutions

**NOTE:** All solutions are provided outside FSG hours, and are not endorsed neither explicitly nor implicitly by the UTM RGASC, or the CSC148 teaching staff. These solutions are meant to be used as a reference, and not a replacement for the problem solving process. You are encouraged to attend office hours and ask questions during lectures if there are any parts of the solution that you do not understand.


## Practice Problem I: 
We didn't get to do this one this week, so we'll do it next week instead

## Practice Problem II:

The trick for this question was to decide which approach to use to solve the problem. You can either use iteration or recursion, but iteration is easier

### General Approach:
The key to this problem is to traverse through the entire tree (i.e: root and subtrees) and pay attention to the subtrees. Remember, we defined a *cycle* as a tree-like structure, but where it's not strictly linearly connected. For instance, if we have a tree with a root and two subtrees, and one of the subtrees has a subtree that points back to the root, then we have a cycle.

The general appraoch is to iterate through the three (technically I should say Graph here) and keep track of all the Nodes we've seen so far. If we see a node that we've already seen, then we have a cycle - This is because in a cycle we're going to see the same node more than once.

But how do we do this? Well, there's two ways. We can either use recursion or iteration. Iteration is easier, but recursion is better practice.

### Iterative Solution:

The general approach for this solution is to use a `Queue` ADT to implement a *Level Order Traversal*. We also need some way to keep track of the nodes we've seen so far. We can use a `set` for this, and use the `id` of the node as the key. Now, you may be wondering: Why not use a list? Well, Lists would technically work, they're just slower. Both solutions are valid, but typically `set`s are better for this kind of problem.

```python
class TreeNode:
  """
  Class representing a node in a tree
  """
  # Implementation omitted; Assume it's a standard TreeNode class
  
    def is_cycle(self) -> bool:
        """
        Method which determines whether the tree is a cycle or not
        """
        # Create a queue and a set to keep track of the nodes we've seen so far
        q = Queue()
        s = set()

        # Enqueue the first node into the queue; this is the root, and will start our "chain reaction" of enqueuing
        q.enqueue(self)
        while not q.is_empty():
        # Dequeue the node; This is the current node we're going to be working with 
        node = q.dequeue()
        # If we've seen this node before, then we have a cycle
        if id(node) in s:
            return True
        # Otherwise, add the node to the set and enqueue all the children
        s.add(id(node))
        for child in node.children: # This is the "chain reaction" I was talking about. This will keep adding all the children of the tree in 
            q.enqueue(child)          # sequential order to the queue, and we'll keep dequeuing them until the queue is empty. This loop ends once 
                                    # we reach a leaf node. 
        
        # Once we break out of the loop, we know we've traversed the entire tree and found no cycles; return False
        return False
```

This approach goes linearly through each *level* of the tree. If the structure provided is a regular tree, then the traversal should traverse down linearly without going back up to any of the previous nodes. However, if it doesn't strictly go down, then we have a cycle.

Iteration was relatively straight forward since we didn't have to deal with alternating stack frames, and could easily share the nodes we've already seen before with the rest of the tree; Since all we had to do was make sure they were visible in the while-loop

Unfortunately, recursion doesn't allow us to share data easily between stack frames, which is why we will define a helper function to help us out. This helper function will take a parameter that will keep track of the nodes we've seen so far, and will return a boolean value to indicate whether we've seen a cycle or not. The main function will serve as a wrapper to the helper (which will be private to avoid users passing in random lists into the function) and will return the result of the helper function.

### Recursive Solution:

```python
class TreeNode:
  """
  Class representing a node in a tree
  """
  # Implementation omitted; Assume it's a standard TreeNode class
  
    def is_cycle(self) -> bool:
        """
        Method which determines whether the tree is a cycle or not
        """
        # Call the helper function with an empty set as a parameter; This will serve as our method of keeping track of the nodes we've seen so far
        # Obviously when we first start, we haven't seen any nodes yet, hence the empty set
        return self._is_cycle_helper(set())
    
    def _is_cycle_helper(self, seen: set)
        """
        Does the actual work of determining whether the tree is a cycle or not
        Private to avoid people passing in random sets and breaking the function
        """
        # STEP ONE: BASE CASES

        # If we see a node we've already seen, then we have a cycle
        if id(self) in seen:
            return True
        
        seen.add(id(self)) # Add the node to the set; This will update the set for the next recursive call

        for subtree in self.children: # Go through all the subtrees and call the helper function on them
            if subtree._is_cycle_helper(seen): # If any of the subtrees have children that we've already seen before
                return True                    # return true
        # The reason we have to *recurse* into the subtrees here is because it's not guaranteed that the cycle will exist
        # At the next level. We have to dig deep into the tree and make sure none of the subtrees have cycles.

        # If we break out of the loop (or didn't enter it in the first place), then we've traversed the entire tree and found no cycles; return False
        return False
```

Note that these solutions (especially for the recursive one) are **not** the only ones you can do. I saw a lot of really great ways in the FSG where people were using `any`, `all`, and `sum` to approach this recursively which is amazing!! Keep it up guys!!

## Challenge problem! 
What if we used a `list` and instead of appending `id`s, we appended the objects themselves. Outside of affecting the time-complexity, would this change the solution in any way? Would we still be able to use `node in lst`? Think about this and try it out!

## Homework Problem:
Coming soon; You gotta actually try the thing first before I give you the answer....
