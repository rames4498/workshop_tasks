class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

a1=BinaryTreeNode(10)
a2=BinaryTreeNode(15)
a3=BinaryTreeNode(20)
a4=BinaryTreeNode(60)
a5=BinaryTreeNode(14)
a6=BinaryTreeNode(25)
a7=BinaryTreeNode(6)

a1.leftChild=a2
a1.rightChild=a3
a2.leftChild=a4
a2.rightChild=a5
a3.leftChild=a6
a3.rightChild=a7

print("Root Node is:")
print(a1.data) 
print("left child of node is:")
print(a1.leftChild.data)
print("right child of node is:")
print(a1.rightChild.data) 
print("Node is:")
print(a2.data)
