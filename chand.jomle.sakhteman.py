class node:
    def __init__(self,zarib,tavan):
        self.zarib=zarib#coef
        self.tavan=tavan
        self.next=None
        self.prev=None

class list:
    def __init__(self):
        self.head=node(None)
        self.n=0

    def insert (self,zarib,tavan):
        new_node=node(zarib,tavan)
        new_node.next=self.head
        self.head=new_node

    def display(self):
        current = self.head
        while current :
            print (f"{current.zarib}x^{current.tavan}",end=" ")
            if current.next:
                print("+" , end="")
            current.next
        print()

    def add (self,other_list):
        result = linkedlist()
        current1 = self.head
        current2 = other_list.head

        while current1 and current2:
            if current1.tavan == current2.tavan:
                result.insert(current1.zarib + current2.zarib,current1.tavan)
                current1 = current1.next
                current2 = current2.next

            elif current1.tavan >  current2.tavan:
                result.insert(current1.zarib,current1.tavan)
                current1=current1.next

            else:
               resut.insert(current2.zarib,current1.tavan)
               current2 = current2.next

            while current1:
                result.insert(current1.zarib,current1.tavan)
                current1 = current1.next

            while current2:
                result.insert(current2.zarib,current2.tavan)
                current2 = current2.next

            return result

    def mult(self,other_list):
        result = linkedlist()
        current1 = self.head
        while current1:
            current2=other_list.head
            while curent2:
                new_zarib = current1.zarib*current2.zarib
                new_tavan = current2.tavan+current2.tavan
                result.insert(new_zarib,new_tavan)
                current2 = current2.next
            current1 = current1.next

        return result
