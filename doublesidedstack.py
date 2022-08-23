def push():
    global top1,top2
    if top1-1==top2:
        print("Stack overflow")
    else:
        ele = int(input("Enter the ele = "))
        option = int(input("1 TOP BOTTOM 2 BOTTOM UP"))
        if option==1:
            top1-=1
            a[top1]=ele
        elif option==2:
            top2+=1
            a[top2] = ele
        else:
            print("Invalid choice")

def pop():
    global top1,top2
    option = int(input("POP = 1 TOP BOTTOM 2 BOTTOM UP"))
    if option==1:
        if top1==max:
            print("Stack underflow")
        else:
            print("Deleting = ",a[top1])
            a[top1] = 0
            top1+=1
    elif option==2:
        if top2==-1:
            print("Stack underflow")
        else:
            print("Deleting = ",a[top2])
            a[top2]=0
            top2-=1

def display():
    global top1,top2
    #option = int(input("DISPLAY = 1 TOP BOTTOM 2 BOTTOM UP"))
    for x in a:
        print(x)

    ''' if option==1:
        if top1==max:
            print("FROM TOP NO INSERTION")
        else:
            print("Elements of stack are = ")
            for i in range(top1,max):
                print(a[i])
    elif option==2:
        if top2==-1:
            print("FROM BOTTOM NO INSERTION")
        else:
            print("Elements of stack are = ")
            for i in range(top2,-1,-1):
                print(a[i])'''

def peek():
    global top1,top2
    print("-------------------------------")
    print("Top most element (TOP )= ",a[top1])
    print("Top most element (BOTTOM )= ",a[top2])
    print("-------------------------------")
max = 5
a = [0]*max
top1=max
top2=-1

while True:
    print("1 PUSH 2 POP 3 PEEK 4 DISPLAY 5 EXIT")
    ch = int(input("Enter the choice  = "))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        peek()
    elif ch==4:
        display()
    elif ch==5:
        break
    else:
        print("invalid choice")
