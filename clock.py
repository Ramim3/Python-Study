import datetime
from time import strftime


theclock = strftime("%H:%M:%S")

#clock figuers
zero = { 0: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         2: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         3: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         4: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         5: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         6: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}

one = { 0:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
        1:  ("\u2B1B" "\u2B1B" "\u2B1C" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
        2:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
        3:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
        4:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
        5:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
        6:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}

two = {  0: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1: ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         2: ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         3: ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" ),
         4: ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
         5: ("\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" ),
         6: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}

three= { 0:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         2:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         3:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         4:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         5:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         6:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}

four= { 0:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        1:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        2:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        3:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
        4:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        5:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        6:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" )}
   
five= { 0:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
        1:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" ),
        2:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" ),
        3:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
        4:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        5:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        6:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}

six = {  0: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" ),
         2: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" ),
         3: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         4: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         5: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         6: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}

seven= { 0:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         2:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         3:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" ),
         4:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
         5:  ("\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" ),
         6:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" )}

eight= { 0:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         2:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         3:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         4:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         5:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         6:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}

nine = { 0: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         2: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         3: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         4: ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         5: ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         6: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}

seperator_1 = { 0: ("\u2B1B" "\u2B1B" "\u2B1B"),
            1: ("\u2B1B" "\u2B1C" "\u2B1B"),
            2: ("\u2B1B" "\u2B1C" "\u2B1B"),
            3: ("\u2B1B" "\u2B1B" "\u2B1B"),
            4: ("\u2B1B" "\u2B1C" "\u2B1B"),
            5: ("\u2B1B" "\u2B1C" "\u2B1B"),
            6: ("\u2B1B" "\u2B1B" "\u2B1B")}

seperator_2 = { 0: ("\u2B1B" "\u2B1B" "\u2B1B"),
            1: ("\u2B1B" "\u2B1B" "\u2B1B"),
            2: ("\u2B1B" "\u2B1B" "\u2B1B"),
            3: ("\u2B1B" "\u2B1B" "\u2B1B"),
            4: ("\u2B1B" "\u2B1B" "\u2B1B"),
            5: ("\u2B1B" "\u2B1B" "\u2B1B"),
            6: ("\u2B1B" "\u2B1B" "\u2B1B")}


list_list=list(theclock)
num_2=list_list[0] 
num_3=list_list[1]
num_4=list_list[2]
num_5=list_list[3]
num_6=list_list[4]
num_7=list_list[5]
num_8=list_list[6]
num_9=list_list[7]
n1=int(num_2) 
n2=int(num_3)
n3=int(num_5)
n4=int(num_6)
n5=int(num_8)
n6=int(num_9)


def first_h():
    if n1==0:
        print(zero[0])
        print(zero[1])
        print(zero[2])
        print(zero[3])
        print(zero[4])
        print(zero[5])
        print(zero[6])
    elif n1==1:
        print(one[0])
        print(one[1])
        print(one[2])
        print(one[3])
        print(one[4])
        print(one[5])
        print(one[6])
    elif n1==2:
        print(two[0])
        print(two[1])
        print(two[2])
        print(two[3])
        print(two[4])
        print(two[5])
        print(two[6])
def second_h():
    if n2==0:
        print(zero[0])
        print(zero[1])
        print(zero[2])
        print(zero[3])
        print(zero[4])
        print(zero[5])
        print(zero[6])
    elif n2==1:
        print(one[0])
        print(one[1])
        print(one[2])
        print(one[3])
        print(one[4])
        print(one[5])
        print(one[6])
    elif n2==2:
        print(two[0])
        print(two[1])
        print(two[2])
        print(two[3])
        print(two[4])
        print(two[5])
        print(two[6])
    elif n2==3:
        print(three[0])
        print(three[1])
        print(three[2])
        print(three[3])
        print(three[4])
        print(three[5])
        print(three[6])
    elif n2==4:
        print(four[0])
        print(four[1])
        print(four[2])
        print(four[3])
        print(four[4])
        print(four[5])
        print(four[6])
    elif n2==5:
        print(five[0])
        print(five[1])
        print(five[2])
        print(five[3])
        print(five[4])
        print(five[5])
        print(five[6])
    elif n2==6:
        print(six[0])
        print(six[1])
        print(six[2])
        print(six[3])
        print(six[4])
        print(six[5])
        print(six[6])
    elif n2==7:
        print(seven[0])
        print(seven[1])
        print(seven[2])
        print(seven[3])
        print(seven[4])
        print(seven[5])
        print(seven[6])
    elif n2==8:
        print(eight[0])
        print(eight[1])
        print(eight[2])
        print(eight[3])
        print(eight[4])
        print(eight[5])
        print(eight[6])
    elif n2==9:
        print(nine[0])
        print(nine[1])
        print(nine[2])
        print(nine[3])
        print(nine[4])
        print(nine[5])
        print(nine[6])
def first_m():
    if n3==0:
        print(zero[0])
        print(zero[1])
        print(zero[2])
        print(zero[3])
        print(zero[4])
        print(zero[5])
        print(zero[6])
    elif n3==1:
        print(one[0])
        print(one[1])
        print(one[2])
        print(one[3])
        print(one[4])
        print(one[5])
        print(one[6])
    elif n3==2:
        print(two[0])
        print(two[1])
        print(two[2])
        print(two[3])
        print(two[4])
        print(two[5])
        print(two[6])
    elif n3==3:
        print(three[0])
        print(three[1])
        print(three[2])
        print(three[3])
        print(three[4])
        print(three[5])
        print(three[6])
    elif n3==4:
        print(four[0])
        print(four[1])
        print(four[2])
        print(four[3])
        print(four[4])
        print(four[5])
        print(four[6])
    elif n3==5:
        print(five[0])
        print(five[1])
        print(five[2])
        print(five[3])
        print(five[4])
        print(five[5])
        print(five[6])
    elif n3==6:
        print(six[0])
        print(six[1])
        print(six[2])
        print(six[3])
        print(six[4])
        print(six[5])
        print(six[6])
    elif n3==7:
        print(seven[0])
        print(seven[1])
        print(seven[2])
        print(seven[3])
        print(seven[4])
        print(seven[5])
        print(seven[6])
    elif n3==8:
        print(eight[0])
        print(eight[1])
        print(eight[2])
        print(eight[3])
        print(eight[4])
        print(eight[5])
        print(eight[6])
    elif n3==9:
        print(nine[0])
        print(nine[1])
        print(nine[2])
        print(nine[3])
        print(nine[4])
        print(nine[5])
        print(nine[6])
def second_m():
    if n4==0:
        print(zero[0])
        print(zero[1])
        print(zero[2])
        print(zero[3])
        print(zero[4])
        print(zero[5])
        print(zero[6])
    elif n4==1:
        print(one[0])
        print(one[1])
        print(one[2])
        print(one[3])
        print(one[4])
        print(one[5])
        print(one[6])
    elif n4==2:
        print(two[0])
        print(two[1])
        print(two[2])
        print(two[3])
        print(two[4])
        print(two[5])
        print(two[6])
    elif n4==3:
        print(three[0])
        print(three[1])
        print(three[2])
        print(three[3])
        print(three[4])
        print(three[5])
        print(three[6])
    elif n4==4:
        print(four[0])
        print(four[1])
        print(four[2])
        print(four[3])
        print(four[4])
        print(four[5])
        print(four[6])
    elif n4==5:
        print(five[0])
        print(five[1])
        print(five[2])
        print(five[3])
        print(five[4])
        print(five[5])
        print(five[6])
    elif n4==6:
        print(six[0])
        print(six[1])
        print(six[2])
        print(six[3])
        print(six[4])
        print(six[5])
        print(six[6])
    elif n4==7:
        print(seven[0])
        print(seven[1])
        print(seven[2])
        print(seven[3])
        print(seven[4])
        print(seven[5])
        print(seven[6])
    elif n4==8:
        print(eight[0])
        print(eight[1])
        print(eight[2])
        print(eight[3])
        print(eight[4])
        print(eight[5])
        print(eight[6])
    elif n4==9:
        print(nine[0])
        print(nine[1])
        print(nine[2])
        print(nine[3])
        print(nine[4])
        print(nine[5])
        print(nine[6])
def first_s():
    if n5==0:
        print(zero[0])
        print(zero[1])
        print(zero[2])
        print(zero[3])
        print(zero[4])
        print(zero[5])
        print(zero[6])
    elif n5==1:
        print(one[0])
        print(one[1])
        print(one[2])
        print(one[3])
        print(one[4])
        print(one[5])
        print(one[6])
    elif n5==2:
        print(two[0])
        print(two[1])
        print(two[2])
        print(two[3])
        print(two[4])
        print(two[5])
        print(two[6])
    elif n5==3:
        print(three[0])
        print(three[1])
        print(three[2])
        print(three[3])
        print(three[4])
        print(three[5])
        print(three[6])
    elif n5==4:
        print(four[0])
        print(four[1])
        print(four[2])
        print(four[3])
        print(four[4])
        print(four[5])
        print(four[6])
    elif n5==5:
        print(five[0])
        print(five[1])
        print(five[2])
        print(five[3])
        print(five[4])
        print(five[5])
        print(five[6])
    elif n5==6:
        print(six[0])
        print(six[1])
        print(six[2])
        print(six[3])
        print(six[4])
        print(six[5])
        print(six[6])
    elif n5==7:
        print(seven[0])
        print(seven[1])
        print(seven[2])
        print(seven[3])
        print(seven[4])
        print(seven[5])
        print(seven[6])
    elif n5==8:
        print(eight[0])
        print(eight[1])
        print(eight[2])
        print(eight[3])
        print(eight[4])
        print(eight[5])
        print(eight[6])
    elif n5==9:
        print(nine[0])
        print(nine[1])
        print(nine[2])
        print(nine[3])
        print(nine[4])
        print(nine[5])
        print(nine[6])
def second_s():
    if n6==0:
        print(zero[0])
        print(zero[1])
        print(zero[2])
        print(zero[3])
        print(zero[4])
        print(zero[5])
        print(zero[6])
    elif n6==1:
        print(one[0])
        print(one[1])
        print(one[2])
        print(one[3])
        print(one[4])
        print(one[5])
        print(one[6])
    elif n6==2:
        print(two[0])
        print(two[1])
        print(two[2])
        print(two[3])
        print(two[4])
        print(two[5])
        print(two[6])
    elif n6==3:
        print(three[0])
        print(three[1])
        print(three[2])
        print(three[3])
        print(three[4])
        print(three[5])
        print(three[6])
    elif n6==4:
        print(four[0])
        print(four[1])
        print(four[2])
        print(four[3])
        print(four[4])
        print(four[5])
        print(four[6])
    elif n6==5:
        print(five[0])
        print(five[1])
        print(five[2])
        print(five[3])
        print(five[4])
        print(five[5])
        print(five[6])
    elif n6==6:
        print(six[0])
        print(six[1])
        print(six[2])
        print(six[3])
        print(six[4])
        print(six[5])
        print(six[6])
    elif n6==7:
        print(seven[0])
        print(seven[1])
        print(seven[2])
        print(seven[3])
        print(seven[4])
        print(seven[5])
        print(seven[6])
    elif n6==8:
        print(eight[0])
        print(eight[1])
        print(eight[2])
        print(eight[3])
        print(eight[4])
        print(eight[5])
        print(eight[6])
    elif n6==9:
        print(nine[0])
        print(nine[1])
        print(nine[2])
        print(nine[3])
        print(nine[4])
        print(nine[5])
        print(nine[6])


print(first_h())
print(second_h())
print(first_m())
print(second_m())
print(first_s())
print(second_s())

