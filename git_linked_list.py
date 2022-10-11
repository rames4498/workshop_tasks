
class Node:

    
    def __init__(self, data):
        self.data = data
        self.next_node = None
#let’s create a node that will have a value equal to 5, and print out the value and the pointer to next node:
       
first_node = Node(5)

print(first_node.data)
print(first_node.next_node)

#few more nodes

second_node = Node(7)
third_node = Node(15)

print(second_node.data)
print(third_node.next_node)

#When initialized, a linked list should only have the head node set to NULL, in order to start an empty linked list:
class LinkedList:

    
    def __init__(self):
        self.head = None

'''''
To start adding nodes to a linked list we want the first_node we created to be the head node of the linked list:
'''''
llist = LinkedList()

llist.head = first_node
'''''
This will create a linked list with one node (which will be the head node).

Recall that each node has a reference link set to NULL. In order to create a sequence of nodes, we will set each reference link to point to the next node:
'''''
llist.head.next_node = second_node

second_node.next_node = third_node
'''''
Here we have been adding nodes to the linked list rather manual than programmatically.Next time we will explore to to insert nodes at the end, and the beginning, and at a specific position of the linked lis
A singly linked list can only be traversed in forward direction.

The logic is fairly simple: we will start at the head node, print its current value, and move to the next node (given that the reference link is not NULL).

We will continue moving to the next node as long as the node has data in it.


'''''
class Node:

    
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    
    def __init__(self):
        self.head = None

        
    def print_llist(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node


llist = LinkedList()

llist.head = first_node
llist.head.next_node = second_node
second_node.next_node = third_node

llist.print_llist()

'''''
In this section we will implement a method insert_at_end() for inserting nodes at the end of a linked list (basically appending new nodes) for the LinkedList() class.

Let’s reuse the linked list we have built in the previous section:
We start at the head node:

if the head node exists, then we move to the next node
if the head node is NULL, then the node we want to add becomes the head node
Assuming that the head node exists, we move to the next node (given that the reference link is not NULL).

We will continue moving to the next node as long as the reference link is pointing to another node that has a value and it’s not the last node (with reference link NULL).

Once we reach the last node, we will insert the new node right after it, and have its reference link as NULL.

'''''

class Node:

    
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    
    
    def __init__(self):
        self.head = None
        
    
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next_node is not None:
            last_node = last_node.next_node
            
        last_node.next_node = new_node
        
    
    def print_llist(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node


llist = LinkedList()

llist.insert_at_end(5)
llist.insert_at_end(7)
llist.insert_at_end(15)

llist.print_llist()

'''''
Inserting a node in the beginning of a linked list is much simpler from the logic and code perspective.

The very first node of a linked list is a head node, and if we need to insert a node before it, we should simply have a node that has a reference link to the head node (of course, if there are no nodes in the linked list, then the new node becomes the head node).
'''''
class Node:
    

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    
    
    def __init__(self):
        self.head = None
        
    
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next_node is not None:
            last_node = last_node.next_node
            
        last_node.next_node = new_node
        
        
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next_node = self.head
        self.head = new_node

    
    def print_llist(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node


llist = LinkedList()

llist.insert_at_end(5)
llist.insert_at_end(7)
llist.insert_at_end(15)

llist.insert_at_beginning(9)

llist.print_llist()
#########################################################
'''''
When inserting a node after a given node, the first step is to find the previous node in the linked list.

In order to find the previous node, we will traverse the linked list from its head node, all the way until we find the previous node.

Once we find the previous node, we will change the reference link of a new node from NULL to the reference link of the previous node, and then we will change the reference link of the previous node to the new node.
'''''






class Node:
    

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    
    
    def __init__(self):
        self.head = None
        
    
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next_node is not None:
            last_node = last_node.next_node
            
        last_node.next_node = new_node
        
        
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = newnode
            return

        new_node.next_node = self.head
        self.head = new_node


    def insert_after_node(self, data, previous_node):
        new_node = Node(data)
        
        current_node = self.head
        while current_node.data != previous_node:
            current_node = current_node.next_node
        
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        
        
    def print_llist(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
    def search(self, data):
        #homework
    def delete(self, data):
        #homework

llist = LinkedList()

llist.insert_at_end(5)
llist.insert_at_end(7)
llist.insert_at_end(15)
llist.insert_at_beginning(9)

llist.insert_after_node(10,7)

llist.print_llist()
