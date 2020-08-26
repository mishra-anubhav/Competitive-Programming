s = input("Enter the string: ")
length = len(s)
res = 0
index =0
while index<length:
    res =res + 1
    incr =index
    decr =index
    while(incr<length-1 and s[incr]<=s[incr+1]):
        incr = incr+1
    while(decr<length-1 and s[decr]>=s[decr+1]):
        decr = decr+1
    index = max(incr,decr) + 1
print(res)
            
            
