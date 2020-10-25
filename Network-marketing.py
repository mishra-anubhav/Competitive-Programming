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
else:
    print("TOTAL MEMBERS : 1")
    print("COMMISSION DETAILS")
    print(parent,":250")
