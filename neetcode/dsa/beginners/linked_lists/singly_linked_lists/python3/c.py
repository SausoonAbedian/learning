from typing import List


# Singly Linked List Node
class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes
        # removing a node from the beginning of list easier.
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1  # Index out of bounds or list is empty

    def insert_head(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:  # If list was empty before insertion
            self.tail = new_node

    def insert_tail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def get_values(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


def test1():
    lst = LinkedList()
    lst.insert_head(1)
    lst.insert_tail(2)
    lst.insert_head(0)
    assert lst.remove(1) is True
    assert lst.get_values() == [0, 2]


def test2():
    lst = LinkedList()
    lst.insert_head(1)
    lst.insert_head(2)
    assert lst.get(5) == -1


def test3():
    lst = LinkedList()
    lst.insert_head(1)
    assert lst.remove(0) is True


def test4():
    lst = LinkedList()
    lst.insert_tail(1)
    lst.insert_tail(2)
    assert lst.get(1) == 2
    assert lst.remove(1) is True
    lst.insert_tail(2)
    assert lst.get(1) == 2
    assert lst.get(0) == 1


test1()
test2()
test3()
test4()
