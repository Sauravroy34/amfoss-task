#hi 
lis = []
def sums(n):
    su =0
    for i in range(1,n):
        if i % 3 == 0:
            lis.append(i)           
        elif i %5 ==0:
            lis.append(i)
    
    return sum(lis)
        


p = int(input())
for k in range(p):
    x = int(input())
    print(sums(x))
    lis.clear()

