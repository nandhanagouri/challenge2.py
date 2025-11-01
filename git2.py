list=[100,120,140,150,160,170,180,190,200]
print("order:",list)
reversed=[]
for i in range (len(list)-1,-1,-1):
    reversed.append(list[i])
print("reversed order:",reversed)