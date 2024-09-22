# Author: @Vaibhav Singh(21BCS128)
def bubbleSort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr  

# Author: @Vaibhav Singh(21BCS128)
def mergeSort(arr):
    """
    Sorts an array using the merge sort algorithm.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

#Author: Don Paul

def quickSort(arr):
    """
    Sorts an array using the quick sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quickSort(left) + middle + quickSort(right)


 
def main():
    print("Choose a sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Heap Sort")
    print("7. Shell Sort")

    choice = int(input("Enter the number of the sorting algorithm: "))
    arr = [2, 1, 10, 23, 5, 7, 9, 4]

    if choice == 1:
        sorted_arr = bubbleSort(arr)
        algo_name = "Bubble Sort"
    elif choice == 2:
        sorted_arr = selectionSort(arr)
        algo_name = "Selection Sort"
    elif choice == 3:
        sorted_arr = insertionSort(arr)
        algo_name = "Insertion Sort"
    elif choice == 4:
        sorted_arr = mergeSort(arr)
        algo_name = "Merge Sort"
    elif choice == 5:
        sorted_arr = quickSort(arr)
        algo_name = "Quick Sort"
    elif choice == 6:
        sorted_arr = heapSort(arr)
        algo_name = "Heap Sort"
    elif choice == 7:
        sorted_arr = shellSort(arr)
        algo_name = "Shell Sort"
    else:
        print("Invalid choice. Please select a number between 1 and 7.")
        return

    print(f"Sorted array using {algo_name} is: {sorted_arr}")
    
    if choice in [1, 2, 3]:
        print("Time Complexity: O(n^2)")
        print("Space Complexity: O(1)")
    elif choice in [4, 6]:
        print("Time Complexity: O(n log n)")
        print("Space Complexity: O(n)")
    elif choice == 5:
        print("Time Complexity: O(n log n)")
        print("Space Complexity: O(log n)")
    elif choice == 7:
        print("Time Complexity: O(n^(3/2))")
        print("Space Complexity: O(1)")


if __name__ == "__main__":
    main()
