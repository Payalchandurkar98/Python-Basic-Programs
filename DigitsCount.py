
num = int(input("Enter a number upto 5 digits: "))

if num>=0 and num<=9:
    print(num,"is a 1-digit number")

elif num>=10 and num<=99:
    print(num,"is a 2-digit number")

elif num>=100 and num<=999:
    print(num,"is a 3-digit number")

elif num>=1000 and num<=9999:
    print(num,"is a 4-digit number")

else:
    print(num,"is a 5-digit number")