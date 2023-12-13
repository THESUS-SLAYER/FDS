import array as arr

# Accept the % marks of the students
def accept_perc():
    a = arr.array('f', [])
    no_stud = int(input("Enter the number of students: "))
    for i in range(0, no_stud):
        a.append(float(input("Enter the percentage of student: ")))
    return a

# Function to sort the array in ascending order using quicksort
def quicksort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quicksort(a, low, pi - 1)
        quicksort(a, pi + 1, high)

def partition(a, low, high):
    i = (low - 1)
    pivot = a[high]
    for j in range(low, high):
        if a[j] <= pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return (i + 1)

# Driver code
a = accept_perc()
print("Unsorted array:")
print(a)
quicksort(a, 0, len(a) - 1)
print("\nSorted array:")
print(a)
print("\nTop five scores:")
for i in range(0, 5):
    print(a[i])
