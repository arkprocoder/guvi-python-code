# if, elif, nested if else, else
# num1=int(input("Enter the Num1:\n"))
# num2=int(input("Enter the Num2:\n"))

# if(num1>num2):
#     print('if block is executing')
#     print('num1',num1,'is greater than num2',num2)

# elif(num1==num2):
#     print('elif is executing')
#     print('Num are equal',num1,num2)

# elif(num1<num2 and num2==15):
#     print('i am the second elif is execution')

# else:
#     print('i am a else block')
#     print('num1',num1,'is lesser than num2',num2)


# print('i will execute after the if block if its fails or pass')
# print('okay')
# print(10+10)


if(False):
    print("i am if")
    if(False):
        print("i am first if of if")
    else:
        print("i am else of first if")

        if(True):
            print("True")

else:
    print(" i am else")
    if(False):
        print("i am else if of if")

    elif(True):
        print("i am el if")
    else:
        print("i am else of first else")

        if(True):
            print("True")    