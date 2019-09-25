class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SinglyLinkedlist:
    def __init__(self, head=None):
        self.head = head

    def addLast(self, item):
        new_node = Node(item)
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node

    def addFirst(self, item):
        item = Node(item)
        item.next = self.head
        self.head = item

    def add(self, index, item):
        new_node = Node(item)
        if index == 0:
            self.addFirst(new_node)
        curr = self.head
        count = 0
        while curr is not None:
            if count == index:
                t = curr.next
                curr.next = new_node
                new_node.next = t
                return True
            count += 1
            curr = curr.next
        return False

    def clear(self):
        self.head = None

    def contains(self, item):
        curr = self.head
        while curr is not None:
            if curr.item == item:
                return True
            curr = curr.next
        return False

    def getIndexOf(self, item):
        curr = self.head
        count = 0
        while curr.item is not item:
            if curr.next is None:
                return -1
            count += 1
            curr = curr.next
        return count

    def get(self, index):
        curr = self.head
        count = 0
        while curr is not None:
            if count == index:
                return curr.item
            count += 1
            curr = curr.next
        return None

    def getFirst(self):
        return self.head.item

    def getLast(self):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        return curr.item

    def remove(self, index):
        if self.head is None:
            return False
        temp = self.head
        if index == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(index-1):
            temp = temp.next
        if temp is None and temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next
        return True

    def removeFirst(self):
        if self.isEmpty():
            return False
        self.head = self.head.next
        return True

    def removeLast(self):
        if self.isEmpty():
            return False
        temp = self.head
        prev = temp
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None
        return True

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def reverse_list(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def bubble(self):
        end = None
        while end != self.head:
            start = self.head
            while start.next != end:
                pointer = start.next
                if start.item > pointer.item:
                    start.item, pointer.item = pointer.item, start.item
                start = start.next
            end = start

    def remove_duplicates(self):
        curr = self.head
        while curr.next is not None:
            if curr.item == curr.next.item:
                self.remove(self.getIndexOf(curr.item))
            curr = curr.next

    def printList(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.item)
                temp = temp.next


ll = SinglyLinkedlist()
ll.addFirst(3)
ll.addFirst(11)
ll.addFirst(11)
ll.addLast(20)
ll.addLast(51)
ll.add(2, 4)
ll.addFirst(4)
ll.addFirst(4)
ll.addFirst(4)
ll.addFirst(4)
ll.addFirst(4)
ll.addFirst(4)
ll.addFirst(4)
ll.addFirst(4)
ll.addFirst(20)
ll.addLast(100)
ll.add(6, 100)

print("NORMAL")
# ll.printList()
print("-----------------")
print("REVERSED")
ll.reverse_list()
# ll.printList()
print("-----------------")
print("REMOVE DUPLICATES")
# ll.bubble()
# ll.remove_duplicates()
# ll.printList()

print("-----------------")
print("TESTS")
print("Get Index of: ", ll.getIndexOf(11))
print("Get last: ", ll.getLast())
print("Get first: ", ll.getFirst())
