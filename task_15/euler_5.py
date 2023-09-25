def is_prime(n):
    if n == 2:
        return True
    for i in range(2, n):
      if n % i == 0:
        return False
    return True
  
li = []
num = []
result = 1
def give_prime(n):
    for j in range(2,n+1):
        if is_prime(j) == True:
            li.append(j)
        
    



x = int(input())
for i in range(x):
    p = int(input())
    give_prime(p)
    for i in li:
        j = i
        while i <= p:
            i = i *j
            
        if i >p:
            
            num.append(i)
        
        
  
    for i in num :
        result = result*i
        
    for i in li:
        result = result/i
    print(int(result))

    result =1 
    #print(li)
    #print(num)
    li.clear()
    num.clear()
