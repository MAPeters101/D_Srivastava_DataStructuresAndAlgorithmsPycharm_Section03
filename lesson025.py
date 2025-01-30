class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is: ")
            p = self.start
            while p is not None:
                print(p.info, " ", end='')
                p = p.link
            print()

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return

        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter the number of nodes: "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted: "))
            self.insert_at_end(data)

    def bubble_sort_exdata(self):
        end = None
        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p

    def merge1(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge1(self.start, list2.start)
        return merge_list

    def _merge1(self, p1, p2):
        if p1.info <= p2.info:
            startM = Node(p1.info)
            p1 = p1.link
        else:
            startM = Node(p2.info)
            p2 = p2.link

        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = Node(p1.info)
                p1 = p1.link
            else:
                pM.link = Node(p2.info)
                p2 = p2.link
            pM = pM.link

        # If second list has finished and elements left in first list
        while p1 is not None:
            pM.link = Node(p1.info)
            p1 = p1.link
            pM = pM.link

        # If first list has finished and elements left in second list
        while p2 is not None:
            pM.link = Node(p2.info)
            p2 = p2.link
            pM = pM.link

        return startM

    def merge2(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge2(self.start, list2.start)
        return merge_list

    def _merge2(self, p1, p2):
        if p1.info <= p2.info:
            startM = p1
            p1 = p1.link
        else:
            startM = p2
            p2 = p2.link

        pM = startM
        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = p1
                pM = pM.link
                p1 = p1.link
            else:
                pM.link = p2
                pM = pM.link
                p2 = p2.link

        if p1 is None:
            pM.link = p2
        else:
            pM.link = p1

        return startM

################################################################################

list1 = SingleLinkedList()
list2 = SingleLinkedList()

list1.create_list()
list2.create_list()

list1.bubble_sort_exdata()
list2.bubble_sort_exdata()

print("First List - "); list1.display_list()
print("Second List - "); list2.display_list()

list3 = list1.merge1(list2)
print("Merged List - "); list3.display_list()
print("First List - "); list1.display_list()
print("Second List - "); list2.display_list()

list3 = list1.merge2(list2)
print("Merged List - "); list3.display_list()
print("First List - "); list1.display_list()
print("Second List - "); list2.display_list()



'''
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

    if option == 1:
        list.display_list()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        data = int(input("Enter the element to be searched: "))
        list.search(data)
    elif option == 4:
        data = int(input("Enter the element to be inserted: "))
        list.insert_in_beginning(data)
    elif option == 5:
        data = int(input("Enter the element to be inserted: "))
        list.insert_at_end(data)
    elif option == 6:
        data = int(input("Enter the element to be inserted: "))
        x = int(input("Enter the element after which to insert: "))
        list.insert_after(data, x)
    elif option == 7:
        data = int(input("Enter the element to be inserted: "))
        x = int(input("Enter the element before which to insert: "))
        list.insert_before(data, x)
    elif option == 8:
        data = int(input("Enter the element to be inserted: "))
        k = int(input("Enter the position at which to insert: "))
        list.insert_at_position(data, k)
    elif option == 9:
        list.delete_first_node()
    elif option == 10:
        list.delete_last_node()
    elif option == 11:
        data = int(input("Enter the element to be deleted: "))
        list.delete_node(data)
    elif option == 12:
        list.reverse_list()
    elif option == 13:
        list.bubble_sort_exdata()
    elif option == 14:
        list.bubble_sort_exlinks()
    elif option == 15:
        list.merge_sort()
    elif option == 16:
        data = int(
            input("Enter the element at which cycle has to be inserted: "))
        list.insert_cycle()
    elif option == 17:
        if list.has_cycle():
            print("List has a cycle")
        else:
            print("List does not have a cycle")
    elif option == 18:
        list.remove_cycle()
    elif option == 19:
        break
    else:
        print("Wrong option")
    print()
'''