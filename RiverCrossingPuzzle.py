### Write a Program to implement river crossing puzzle ? Man with a Lion, Goat and Cabbage

 

x=['M','L','G','C']
y=[]
print("Before Process")
print("Element in the left  side",x)
print("Element in the Right side",y)
while True:
    print(x[1]," ",x[2]," ",x[3], " Select any one from the list.")
    i=input("Enter the item: ")
    i=i.upper()
    if x[1]==i and x[2]=='G' and x[3]=='C':
        print("Goat will eat Cabbage :")
        break
    elif x[2]==i and x[3]!='C':
        y.append(x[2])
        if len(y)==2 and y[0]=='G':
            x[2]=y[0]
            y[0]=y[1]
            y.pop()
    elif x[1]==i and x[2]=='G':
        y.append(x[1])
        x[1]=x[2]
        x[2]=''
        if len(y)==2 and y[0] =='G':
            x[2]=y[0]
            y[0]=y[1]
            y.pop()

    elif x[1]==i and x[2]!='C' and x[2]!='G':
        y.append(x[1])
        y.append('M')
        x[1]==''
        x=[]
        print("Goal is reached")
        break
    if x[2]==i and x[3]=='C':
        y.append(x[2])
        x[2]=x[3]
        x[3]=''
    if x[3]==i:
        print("Lion will eat Goat :")
        break

 

print("After Process")
print("Element in the Left Side Bank ",x)
print("Element in the Right Side Bank ",y)

 