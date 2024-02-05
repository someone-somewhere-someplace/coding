import random

First = []
Reversed = []
for x in range(100):
    First.append(random.randint(1,10))
Item_Num = 100
help = 1
for y in range(100):
    Reversed.append(First[Item_Num - help])
    Item_Num = Item_Num - 1
print(f"{First}, and,{Reversed}")
