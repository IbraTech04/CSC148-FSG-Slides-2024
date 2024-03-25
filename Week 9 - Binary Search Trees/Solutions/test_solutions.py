from solutions import *

lst1 = [1,2,3,4,5]
tree1 = BinarySearchTree(5)
for i in lst1:
    tree1.insert(i)

assert reconstruct_from_postorder(tree1.postorder()) == tree1
assert reconstruct_from_preorder(tree1.preorder()) == tree1

lst2 = [5,2,3,6,9,8,7,5,4]
tree2 = BinarySearchTree(5)
for i in lst2:
    tree2.insert(i)

assert reconstruct_from_postorder(tree2.postorder()) == tree2
assert reconstruct_from_preorder(tree2.preorder()) == tree2

lst3 = [11,2,5,8,9,66,4,7,4,1,54,964884,351,5]
tree3 = BinarySearchTree(11)
for i in lst3:
    tree3.insert(i)

assert reconstruct_from_postorder(tree3.postorder()) == tree3
assert reconstruct_from_preorder(tree3.preorder()) == tree3

