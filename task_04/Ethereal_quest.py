def check(force):

  sum_xi = 0
  sum_yi = 0
  sum_zi = 0

  for xi, yi, zi in force:
    sum_xi += xi
    sum_yi += yi
    sum_zi += zi

  return sum_xi == 0 and sum_yi == 0 and sum_zi == 0
    





force = []
q = int(input())
for i in range(q):
    force.append([int(x) for x in input().split()])
if check(force) == True:
    print("YES")
else:
    print("NO")
        
