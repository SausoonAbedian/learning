from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None


class LinkedList:

    def __init__(self):
        self.hd = Node(-1)
        self.tl = self.hd

    def get(self, index: int) -> int:
        cr = self.hd.nxt
        while cr and index > 0:
            cr = cr.nxt
            index -= 1
        if not cr or index != 0:
            return -1
        return cr.val

    def insert_head(self, val: int) -> None:
        node = Node(val)
        node.nxt = self.hd.nxt
        self.hd.nxt = node
        if not node.nxt:
            self.tl = node

    def insert_tail(self, val: int) -> None:
        node = Node(val)
        self.tl.nxt = node
        self.tl = self.tl.nxt

    def remove(self, index: int) -> bool:
        prev = self.hd
        while prev.nxt and index > 0:
            index -= 1
            prev = prev.nxt
        if not prev.nxt or index != 0:
            return False
        prev.nxt = prev.nxt.nxt
        if not prev.nxt:
            self.tl = prev
        return True

    def get_values(self) -> List[int]:
        lst = []
        cr = self.hd.nxt
        while cr:
            lst.append(cr.val)
            cr = cr.nxt
        return lst


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
