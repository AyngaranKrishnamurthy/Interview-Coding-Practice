import heapq

lst = [2,5,3,6,2,7,1]
lst1 = [3,5,2,6,8,5,9,5]

############################################################### MinHeap ###############################################################
heapq.heapify(lst)
print("1. Min Heap: ",lst)

small = heapq.heappop(lst)
print("2. Smallest Element popped out from the list: ",small)

peeksmall = lst[0]
print("3. Peek the smallest element of the heap: ",peeksmall)

############################################################### MaxHeap ###############################################################
maxheap = [-num for num in lst1]# Convert to a max-heap by negating the values
heapq.heapify(lst1)
print("4. Max Heap: ",[-x for x in maxheap])# Convert back to positive to display

largest = -heapq.heappop(maxheap)
print("5. Largest Element popped out from the list:", largest)

peek_largest = -maxheap[0]
print("6. Peek the largest element of the heap:", peek_largest)


