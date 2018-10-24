one = input("Enter an integer:")

two = input("Enter another:")

try:
    one = int(one)
    two = int(two)
    if one == two:
        print(one +" and "+ two + " are equal!")
    else:
        print(one +" and "+ two + " are not equal.")
    if one > two:
        print(one +" is greater than "+ two + "!")
    elif one < two:
        print(one +" is less than " + two +"!")
except:
    if type(one) != int:
        print("Enter an INTEGER.")
    elif type(two) != int:
        print("Enter an INTEGER.")
