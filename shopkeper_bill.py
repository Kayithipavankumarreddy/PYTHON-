ch=input()
total=0
while ch =="y":
    item_cost=int(input())
    quantity=int(input())
    total=total+(item_cost*quantity)
    ch=input()
print(total)
