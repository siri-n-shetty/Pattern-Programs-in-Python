row = 5
asci = 65
incr=1
for i in range(0,row):
    for j in range(0,incr):
        print(chr(asci),end="")
        asci +=1
    incr+=2
    print()