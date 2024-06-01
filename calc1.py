a=int(input("enter number 1"))
b=int(input("enter number 2"))

printf(" options : ADD SUB MUL DIV")
choice=int(input("enter choices 1-4"))

if choice==1:
    add(a,b)
elif choice==2:
    sub(a,b)
elif choice==3:
    mul(a,b)
elif choice==4:
    div(a,b)
def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def mul(a,b):
    c=a*b
    print(c)
def div(a,b):
    c=a//b
    print(c)
