# Bubble sort and display top five scores
def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = []
print("*************bubble_Sort***************")
Num = int(input("Enter the number of students "))
for i in range(Num):
    per = float(input("Enter the percentage marks "))
    arr.append(per)

bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%f" % arr[i])

# Selection Sort
def selectionSort(arr1):
    for i in range(len(arr1)):
        min_idx = i
        for j in range(i + 1, len(arr1)):
            if arr1[min_idx] > arr1[j]:
                min_idx = j
        # Swap the found minimum element with
        # the first element
        arr1[i], arr1[min_idx] = arr1[min_idx], arr1[i]

arr1 = []
print("******selection_sort*********")
Num = int(input("Enter the number of students "))
for i in range(Num):
    per = float(input("Enter the percentage marks "))
    arr1.append(per)

selectionSort(arr1)
# Driver code to test above
print("Sorted array")
for i in range(len(arr1)):
    print("%f" % arr1[i])
