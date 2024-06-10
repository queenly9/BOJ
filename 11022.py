case = int(input())
for i in range(case):
  a, b = map(int, input().split())
  c = a + b
  print("Case #"+str(i+1)+":",a,"+",b,"=",c)