def check(n):
    return str(n) == str(n)[::-1]
lis = []
def product(n):
  
    for i in range(100, 999):
      for j in range(100,999):
        product = i * j
        if product < n and check(product):
            lis.append(product)
         
    return max(lis)
 
t = int(input())
  
  
for i in range(t):
  
    n = int(input())
    print(product(n))
    lis.clear()
    
