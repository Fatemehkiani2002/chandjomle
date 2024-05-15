class node:
    def __init__(self,zarib,tavan):
        self.zarib=zarib
        self.tavan=tavan
        self.next=None
        self.prev=None

class polynimialMenu:
    def __init__(self):
        self.poly = None
        self.head=node(None)
        self.n=0

    def insert (self,zarib,tavan):
        new_node=node(zarib,tavan)
        new_node.next=self.head
        self.head=new_node

    def print (self):
        current = self.head
        while current :
            print (f"{current.zarib}x^{current.tavan}",end=" ")
            if current.next:
                print("+" , end="")
            current.next
        print()

    def sum (self,other_list):
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

    def run_menu(self):
        while true:
            print("1.insert a polynomils")
            print("2.sum two polynomials")
            print("3.mult two polynomials")
            print("4.print")
            print("5.exit")


            choice = int(input("enter your celection:"))
            if choice == 1:
                self.insert()
            elif choice == 2:
                self.sum()
            elif choice == 3:
                self.mult()
            elif choice == 4:
                self.print()
            elif choice == 5:
                break
            else:
                print("invalid choice! please try again.")
        
#main:
#im_not_sure

poly1:polynimialMenu()
poly1:(3,2)
poly1:(5,1)
poly1:(7,0)

poly2:polynomial()
poly2:(4,3)
poly2:(6,0)

print("polynomial 1",end="")
poly1.display()

print("polynomial 2",end="")
poly2.display()

sum_result = poly1.add(poly2)
print("sumation: ",end="")
sum_result.display()

product_result = poly1.mult(poly2)
print("mult: ",end="")
product_result.display()

