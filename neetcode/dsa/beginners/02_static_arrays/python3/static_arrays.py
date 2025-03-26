# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insert_end(arr, n, length, capacity):
    if length < capacity:
        arr.append(n)
        length += 1


# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).
def remove_end(arr, length):
    if length > 0:
        length -= 1
        del arr[length - 1]


# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insert_middle(arr, i, n, length):
    arr.append(0)
    for j in range(length, i, -1):
        arr[j] = arr[j - 1]
    arr[i] = n
    length += 1


# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def remove_middle(arr, i, length):
    for j in range(i, length - 1):
        arr[j] = arr[j + 1]
    del arr[length - 1]
    length -= 1


def print_arr(arr, capacity):
    print(arr)


arr = []

print('Testing insert_end\n')

insert_end(arr, 10, 0, 5)
print(f"n = {10}, length = {0}, capacity = {5}, arr = {arr}")
insert_end(arr, 11, 1, 5)
print(f"n = {11}, length = {1}, capacity = {5}, arr = {arr}")
insert_end(arr, 12, 2, 5)
print(f"n = {12}, length = {2}, capacity = {5}, arr = {arr}")
insert_end(arr, 13, 3, 5)
print(f"n = {13}, length = {3}, capacity = {5}, arr = {arr}")
insert_end(arr, 14, 4, 5)
print(f"n = {14}, length = {4}, capacity = {5}, arr = {arr}")

print('\nTesting insert_middle\n')

insert_middle(arr, 4, 20, 5)
print(f"i = {5}, n = {20}, length = {5}, arr = {arr}")
insert_middle(arr, 0, 21, 6)
print(f"i = {0}, n = {21}, length = {6}, arr = {arr}")
insert_middle(arr, 3, 22, 7)
print(f"i = {3}, n = {22}, length = {7}, arr = {arr}")


print('\nTesting remove_middle\n')

remove_middle(arr, 7, 8)
print(f"i = {7}, length = {8}, arr = {arr}")
remove_middle(arr, 0, 7)
print(f"i = {0}, length = {7}, arr = {arr}")
remove_middle(arr, 3, 6)
print(f"i = {3}, length = {6}, arr = {arr}")

print('\nTesting remove_end\n')

remove_end(arr, 5)
print(f"length = {5}, arr = {arr}")
remove_end(arr, 4)
print(f"length = {4}, arr = {arr}")
remove_end(arr, 3)
print(f"length = {3}, arr = {arr}")
remove_end(arr, 2)
print(f"length = {2}, arr = {arr}")
remove_end(arr, 1)
print(f"length = {1}, arr = {arr}")
remove_end(arr, 0)
print(f"length = {0}, arr = {arr}")
