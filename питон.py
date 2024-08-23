list=[1,2,3]
count=len(list)
if count%2 == 0:
    print([list[:count//2],list[count//2:]])
else:
    print([list[:count // 2+1], list[count // 2+1:]])


