num=int(input("enter the limit: "))
c=[]
for i in range(1,num+1):
    item=int(input("enter the element: "))
    c+=[item]
print(sorted(c))
