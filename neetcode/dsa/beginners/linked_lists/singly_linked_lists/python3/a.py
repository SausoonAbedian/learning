from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None


class LinkedList:

    def __init__(self):
        self.hd = None
        self.tl = None

    def get(self, index: int) -> int:
        cr = self.hd
        while cr is not None and index != 0:
            cr = cr.nxt
            index -= 1
        if cr is not None:
            return cr.val
        return -1

    def insert_head(self, val: int) -> None:
        if self.hd is None:
            self.hd = Node(val)
            self.tl = self.hd
        elif self.hd == self.tl:
            self.hd = Node(val)
            self.hd.nxt = self.tl
        else:
            tmp = Node(val)
            tmp.nxt = self.hd
            self.hd = tmp

    def insert_tail(self, val: int) -> None:
        if self.tl is None:
            self.tl = Node(val)
            self.hd = self.tl
        elif self.tl == self.hd:
            self.tl = Node(val)
            self.hd.nxt = self.tl
        else:
            tmp = Node(val)
            self.tl.nxt = tmp
            self.tl = self.tl.nxt

    def remove(self, index: int) -> bool:
        if index < 0 or self.hd is None:
            return False
        elif index == 0:
            self.hd = self.hd.nxt
            return True
        prev = self.hd
        index -= 1
        while prev.nxt is not None or index < 0:
            if index == 0:
                break
            prev = prev.nxt
            index -= 1
        if prev.nxt is None or index < 0:
            return False
        prev.nxt = prev.nxt.nxt
        if self.hd is None or self.hd.nxt is None:
            self.tl = self.hd
        return True

    def get_values(self) -> List[int]:
        arr = []
        curr = self.hd
        while curr is not None:
            arr.append(curr.val)
            curr = curr.nxt
        return arr


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
