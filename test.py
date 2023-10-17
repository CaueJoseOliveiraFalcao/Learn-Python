a = 0 
for i in range(30):
    if a % 2 == 0:
        a+= 1
    else :
        if a % 5 == 0:
            break
        else:
            a += 3
print (a)