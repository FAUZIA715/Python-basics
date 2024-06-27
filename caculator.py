class calculator(): 
    def add(self):
        print(a+b)
    def subs(self):
        print(a-b)
    def div(self):
        print(a/b)
    def mul(self):
        print(a*b)
a=int(input("enter the first number"))
b=int(input("enter the second number"))
obj=calculator()
choice=1
while(choice!=0):
    choice=int(input("enter the choice 1 for addition,2 for sub,3 for division ,4 for multiplication"))
    if(choice==1):
        obj.add()
    elif(choice==2):
        obj.subs()
    elif(choice==3):
        obj.div()
    elif(choice==4):
        obj.mul()
    elif(choice==5):
        exit()
    else:
        print("inavalid choice")
    