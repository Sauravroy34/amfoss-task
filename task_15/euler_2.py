li = [1,2]
sums = [] 
x = int(input())
for j in range(x):
    p = int(input())
    for k in range(p):
            li.append(li[-1]+li[-2])
        
    for m in li:
        if m%2 == 0:
            sums.append(m)
            if m>p:
                break
    if sum(sums) == p:
        print(sum(sums))
        sums.clear()
    elif sum(sums)>p:
        sums.pop()
        print(sum(sums))

        sums.clear()

