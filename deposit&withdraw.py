def deposit(num):
    global balance
    balance = balance + num
def withdrawa(num):
    global balance
    if (balance > num):
       balance = balance - num
list1 = []
balance = 0
while True:
    data = input("please enter the transaction details:\n")
    if 'Exit' == data:
        break
    list1.append(data.split())
print(list1)
for var in list1:
    if (var[0] == 'D'):
        deposit(int(var[1]))
    elif (var[0] == 'W'):
        withdrawa(int(var[1]))
print("balance is:",balance)
