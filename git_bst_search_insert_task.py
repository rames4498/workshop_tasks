class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild=None

  def insert(root,newValue):
    #if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root=BinaryTreeNode(newValue)
        return root
    #binary search tree is not empty, so we will insert it into the tree
    #if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue<root.data:
        root.leftChild=insert(root.leftChild,newValue)
    else:
        #if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild=insert(root.rightChild,newValue)
    return root
  def search(root,value):
    #Condition 1
    if root==None:
        return False
    #Condition 2
    elif root.data==value:
        return True
    #Condition 3
    elif root.data <value:
        return search(root.rightChild,value)
    # Condition 4
    else:
        return search(root.leftChild,value)
# Homework
  #def maximumValue()
  #def minimumValue()
root= insert(None,15)
insert(root,10)
insert(root,25)
insert(root,6)
insert(root,14)
insert(root,20)
insert(root,60)
a1=root
a2=a1.leftChild
a3=a1.rightChild
a4=a2.leftChild
a5=a2.rightChild
a6=a3.leftChild
a7=a3.rightChild
print("Root Node is:")
print(a1.data)
print("left child of node is:")
print(a1.leftChild.data)
print("right child of node is:")
print(a1.rightChild.data)
