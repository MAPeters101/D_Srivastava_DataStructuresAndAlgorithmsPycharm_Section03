from urllib.parse import parse_qsl


class Node:
    def __init__(self,value):
        self.info = value
        self.link = not None
        
class SingleLinkedList:
    def __init__(self):
        self.start = None
        
    def display_list(self):
        pass
    
    def count_nodes(self):
        pass
    
    def search(self,x):
        pass
    
    def insert_in_beginning(self,data):
        pass
    
    def insert_at_end(self,data):
        pass
    
    def create_list(self):
        pass
    
    def insert_after(self,data,x):
        pass
    
    def insert_before(self,data,x):
        pass
    
    def insert_at_position(self,data,k):
        pass

    def delete_node(self,x):
        pass

    def delete_first_node(self):
        pass

    def delete_last_node(self):
        pass

    def reverse_list(self):
        pass

    def bubble_sort_exdata(self):
        pass

    def bubble_sort_exlinks(self):
        pass

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self,x):
        pass

    def merge2(self,list2):
        pass

    def _merge2(self,p1,p2):
        pass

    def merge_sort(self):
        pass

    def _merge_sort_rec(self,listStart):
        pass

    def _divide_list(self,p):
        pass

################################################################################

list = SingleLinkedList()
list.create_list()

while True:
    print("1. Display list")
    print("2. Count the number of nodes")
    print("3. Search for an element")
    print("4. Insert in empty list/Insert in beginning of the list")
    print("5. Insert a node at the end of the list")
    print("6. Insert a node after a specified node")
    print("7. Insert a node before a specified node")
    print("8. Insert a node at a given position")
    print("9. Delete first node")
    print("10. Delete last node")
    print("11. Reverse the list")
    print("13. Bubble sort by exchanging data")
    print("14. Bubble sort by exchanging links")
    print("15. MergeSort")
    print("16. Insert Cycle")
    print("17. Detect Cycle")
    print("18. Remove Cycle")
    print("19. Quit")

    option = int(input("enter your choice: "))






