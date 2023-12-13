# To display word with the longest length
str1 = input("Enter the string to display the word with the longest length:\n")
# split the string into words
list1 = str1.split()
max_length = 0
longest_word = ""

for word in list1:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print("The word with the longest length:", longest_word)

# To check whether the given string is a palindrome or not
string = input("Enter a string:")
if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# To determine the frequency of occurrence of a particular character in the string
str1 = input("Enter the string to count the frequency of a particular character:\n")
char = input("Enter character: ")
counter = 0

for i in range(len(str1)):
    if char == str1[i]:
        counter += 1

print("Character", char, "is present", counter, "times in the string", str1)

# To count the occurrences of each word in a given string
str1 = input("Enter input string:")
str1 = str1.split()  # Split the string into a list

word_count = {}
for word in str1:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")

# To display the index of the first appearance of the substring (find() used)
str1 = input("Enter the string to display the index of the first appearance of the substring:\n")
sub1 = input("Enter substring:\n")
index = str1.find(sub1)

if index != -1:
    print(f"Index of the first appearance of '{sub1}': {index}")
else:
    print(f"'{sub1}' not found in the string.")
