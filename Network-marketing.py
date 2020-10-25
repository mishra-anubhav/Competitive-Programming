parent = input()
ques = input()
if ques=='Y':
    list = input()
    list = list.split(',')
    n = len(list)
print("TOTAL MEMBERS :",n)
print("COMMISSION DETAILS")
print(parent,":",(n*500))
for i in list:
    print(i,": 250")
