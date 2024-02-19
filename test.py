# algorithm to return the largest and second largest number and the smallest and second smallest number in an array

arr1 = [10,7,13,23,54,23]

def largestSmallest(arr):
    largest = arr[0]
    second_largest = arr[0]
    smallest = arr[0]
    second_smallest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest:
            second_largest = arr[i]
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i] < second_smallest:
            second_smallest = arr[i]
    return largest, second_largest, smallest, second_smallest


print(largestSmallest(arr1)) # (54, 23, 7, 10)

    
  

