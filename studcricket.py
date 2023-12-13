# List holding names of students
groupA = ["ram", "pranav", "yash", "sahil"]
groupB = ["ram", "atharva", "rohan", "raj", "yash"]
groupC = ["pranav", "sahil", "omkar", "yash"]

# List of students who play both cricket and badminton
print("List of students who play both cricket and badminton")
resultlistCB = [student for student in groupB if student in groupA]
print(resultlistCB)

# List of students who play either cricket or badminton but not both
print("List of students who play either cricket or badminton but not both")
resultlistCBN = []
flag = 0

if len(groupA) < len(groupB):
    for student in groupB:
        for var in groupA:
            if student == var:
                flag = 1
                break
        if flag == 0:
            resultlistCBN.append(student)
        flag = 0
else:
    for student in groupA:
        for var in groupB:
            if student == var:
                flag = 1
                break
        if flag == 0:
            resultlistCBN.append(student)
        flag = 0

print(resultlistCBN)

# Number of students who play neither cricket nor badminton (only football)
print("Number of students who play neither cricket nor badminton")
resultlistCBNF = []
for student in groupC:
    for var in groupA:
        if student == var:
            flag = 1
            break
    for var1 in groupB:
        if student == var1:
            flag = 1
            break
    if flag == 0:
        resultlistCBNF.append(student)
    flag = 0

print(resultlistCBNF)

# List of students who play cricket and football but not badminton
print("List of students who play cricket and football but not badminton")
resultlistCF = [student for student in groupC if student in groupA]
resultlistNB = []
flag = 0

for student in resultlistCF:
    for var in groupB:
        if student == var:
            flag = 1
            break
    if flag == 0:
        resultlistNB.append(student)
    flag = 0

print(resultlistNB)
