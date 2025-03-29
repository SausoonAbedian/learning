class DynamicArray:

    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.idx = -1

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def push_back(self, n: int) -> None:
        if self.idx >= self.capacity - 1:
            self.resize()
        self.idx += 1
        self.arr[self.idx] = n

    def pop_back(self) -> int:
        tmp = self.arr[self.idx]
        self.arr[self.idx] = -999
        self.idx -= 1
        return tmp

    def resize(self) -> None:
        self.capacity *= 2
        temp_arr = [0] * self.capacity
        for i in range(0, len(self.arr)):
            temp_arr[i] = self.arr[i]
        self.arr = temp_arr

    def get_size(self) -> int:
        return self.idx + 1

    def get_capacity(self) -> int:
        return self.capacity


def case1() -> None:
    arr = DynamicArray(1)
    assert arr.get_size() == 0
    assert arr.get_capacity() == 1


def case2() -> None:
    arr = DynamicArray(1)
    arr.push_back(1)
    assert arr.get_capacity() == 1
    arr.push_back(2)
    assert arr.get_capacity() == 2


def case3() -> None:
    arr = DynamicArray(1)
    assert arr.get_size() == 0
    assert arr.get_capacity() == 1
    arr.push_back(1)
    assert arr.get_size() == 1
    assert arr.get_capacity() == 1
    arr.push_back(2)
    assert arr.get_size() == 2
    assert arr.get_capacity() == 2
    assert arr.get(1) == 2
    arr.set(1, 3)
    assert arr.get(1) == 3
    assert arr.pop_back() == 3
    assert arr.get_size() == 1
    assert arr.get_capacity() == 2


case1()
case2()
case3()
