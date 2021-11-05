def cal(num1, num2, op) :
    ans = 0
    if op == '+' : 
      ans = num1 + num2 
      print(num1,'+',num2,' = ',ans)
    elif op=='-':
      ans = num1 - num2 
      print(num1,'-',num2,' = ',ans)
    elif op=='*':
      ans = num1 * num2 
      print(num1,'*',num2,' = ',ans)
    elif op=='/':
      ans = num1 / num2 
      print(num1,'/',num2,' = ',ans)
a=int(input())
b=int(input())
c=input()
print(cal(a,b,c))