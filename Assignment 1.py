
#Urrete, Jonathan U.

for row in range(6):
    for col in range(23):
        if (col == 0 or col == 4) or (row == 1 and col == 1) or (row==3 and col==3) or (row==2 and col==2) or \
                ((row==0 or row==5) and col>6 and col<10) or ((col==6 or col==10) and (row>0 and row<5)) or \
                ((row==0 or row==5) and (col>11 and col<16)) or ((col==12 or col==16) and (row>0 and row<5)) or \
                ((row==0 or row==5) and col>17) or (col==20 and (row>0 and row<5)):
            print("*",end="")
        else:
            print(end=" ")
    print()
