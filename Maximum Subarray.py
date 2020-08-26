t = int(input())
b = 0
while(b < t):
    a = list(map(int,input().split(" ")))
    k = int(input())
    g = 0
    s = 0
    e = 0
    res = 0
    for i in a:
        if i > k:
            g+=1
        elif i < k:
            s+=1
        else:
            e+=1
    if (g == 0 or s==0) and (a[0] == k or a[len(a)-1]==k):
        res = 1
    else:  
        if g>s:
            diff = g-s
            count = 0
            flag = 0
            for i in range(len(a)):
                if a[i] > k:
                    count+=1 
                else:
                    count = 0
                if count == diff:
                    flag = 1 
                    break
            if flag == 1:
                res = (s*2) + e
            else:
                res = 0
        if g<s:
            diff = s-g
            count = 0
            flag = 0
            for i in range(len(a)):
                if a[i] < k:
                    count+=1 
                else:
                    count = 0
                if count == diff:
                    flag = 1 
                    break
            if flag == 1:
                res = (g*2) + e
            else:
                res = 0
        if g == s:
            res = len(a)
    print(res)
    b+=1
