#question1
a = input("enter a string which is odd length and greater than 7: ")
if len(a) > 7 and len(a) % 2 == 1:
    mid = len(a) // 2
    middle_three = a[mid-1 : mid+2]
    print(middle_three)
else:
    print("invalid input!please enter a string with odd length greater than 7")


#question2
a = input("please enter 8 elements without spaces: ")
if len(a) == 8:
    first=tuple(a[4:8])   # elements 4,5,6,7
    second= tuple(a[0:4])  # elements 0,1,2,3
    output= first + second
    print(output)
else:
    print("invalid input! please enter exactly 8 characters")

#question3
#Write the output of the following program : i)x=10 ii) x=20 iii)x=9
x = int(input("enter a value of x: "))
if x != 10:
    print(x + 1)
elif x <= 10:
    print(x + 2)
    if x <= 20:
        print(x + 3)
    else:
        print(x + 4)
else:
    print(x + 5)


# outputs:
#  i) 12, 13
#  ii) 21
#  iii) 10