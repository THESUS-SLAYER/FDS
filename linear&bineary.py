def accept_student_roll_numbers():
    n = int(input("Enter the total number of students: "))
    student_roll_numbers = []
    for i in range(n):
        roll_no = int(input("Enter the roll no of student %d: " % (i + 1)))
        student_roll_numbers.append(roll_no)
    print("Student info accepted successfully\n\n")
    return student_roll_numbers, n

def display_student_roll_numbers(student_roll_numbers, n):
    if n == 0:
        print("\nNo records in the database")
    else:
        print("Students Array:", end=' ')
        for roll_no in student_roll_numbers:
            print("%d  " % roll_no, end=' ')
        print("\n")

def linear_search(student_roll_numbers, n, X):
    for i in range(n):
        if student_roll_numbers[i] == X:
            return i  # found, so returning the position (index)
    return -1  # not found

def binary_search(student_roll_numbers, X):
    low, high = 0, len(student_roll_numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if student_roll_numbers[mid] == X:
            return mid  # found, so returning the position (index)
        elif student_roll_numbers[mid] < X:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # not found

def main():
    student_roll_numbers = []
    while True:
        print("\t1: Accept & Display Students info ")
        print("\t2: Linear Search")
        print("\t3: Binary Search (Assuming the array is sorted)")
        print("\t4: Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if choice == 4:
            print("End of Program")
            break
        elif choice == 1:
            student_roll_numbers, n = accept_student_roll_numbers()
            display_student_roll_numbers(student_roll_numbers, n)
        elif choice == 2:
            X = int(input("Enter the roll_no to be searched: "))
            result = linear_search(student_roll_numbers, n, X)
            display_search_result(result)
        elif choice == 3:
            X = int(input("Enter the roll_no to be searched: "))
            student_roll_numbers.sort()  # Assuming the array is sorted
            result = binary_search(student_roll_numbers, X)
            display_search_result(result)
        else:
            print("Wrong choice entered! Try again")

def display_search_result(result):
    if result == -1:
        print("\tRoll no to be searched not found\n")
    else:
        print("\tRoll no found at location %d" % (result + 1))

# Example usage:
main()
