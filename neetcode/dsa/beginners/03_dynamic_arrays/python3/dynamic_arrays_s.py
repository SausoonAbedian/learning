# Dynamic Array implementation
# Note: Python lists are dynamic arrays by default,
# but this is an example of what's going on under the hood.
class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    # Get value at i-th index
    def get(self, i: int) -> int:
        return self.arr[i]

    # Set n at i-th index
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # Insert n in the last position of the array
    def push_back(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    # Remove the last element in the array
    def pop_back(self) -> int:
        if self.length > 0:
            # soft delete the last element
            self.length -= 1
        # return the popped element
        return self.arr[self.length]

    def resize(self) -> None:
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        # Copy elements to new_arr
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def get_size(self) -> int:
        return self.length

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
