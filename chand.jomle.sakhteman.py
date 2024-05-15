class node:
    def __init__(self,zarib,data )
        self.zarib=zarib
        self.data=data
        self.next=none
        self.prev=none

class list:
    def __init__(self):
        self.head=node(none)
        self.n=0

    def insert (self,zarib,data):
        new_node=node(zarib,data)
        new_node.next=self.head
        self.head=new_node

    def display(self):
        

    
        

    
