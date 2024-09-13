#Author: @Vaibhav Singh(21BCS128)
def bubbleSort(arr):
    
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            
        
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])
                
arr = [ 2, 1, 10, 23 ]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])
