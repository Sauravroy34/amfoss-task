def check(n):
    if n==2:
        return True
    for i in range(2,n):
        if n % i ==0:
            return False
            
    return True
        
        
        
        
prime = []
x = int(input())
for i in range(x):
    p = int(input())
    for i in range(1,p+1):
        if p %i == 0:
            if check(i) == True:
                 prime.append(i)
    
    print(max(prime))
    prime.clear()
        
