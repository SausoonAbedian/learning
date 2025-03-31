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
        while cr != None and index != 0:
            cr = cr.nxt
            index -= 1
        if cr != None:
            return cr.val
        return -1

    def insertHead(self, val: int) -> None:
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

    def insertTail(self, val: int) -> None:
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
        pass

    def get_values(self) -> List[int]:
        pass