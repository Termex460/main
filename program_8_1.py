from random import randint
from time import time

def linear_search(data, key):
    key_index = -1
    for i in range(len(data)):
        if data[i] == key:
            key_index = i
            break
    return key_index

def binary_search(data, key):
    key_index = -1
    left = 0
    right = len(data) - 1
    mid = (left + right) // 2
    while left < right:
        if data[mid] == key:
            key_index = mid
            break
        elif data[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
    return key_index
 
def bubble_sort(data):
    for j in range(len(data) - 1):
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
        print(*data)


f = open("m1_sorted.txt")
data = [int(x) for x in f]

begin_time = time()
bubble_sort(data)
end_time = time()
print(int((end_time - begin_time) * 1000))

#k = int(input())
#print(linear_search(data, k), binary_search(data, k))

