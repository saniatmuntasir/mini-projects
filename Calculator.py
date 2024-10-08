result = int(input("Take any number: "))
while True:
    print("Operations: '1 for Addition','2 for Substraction','3 for Multiplication','& 4 for Division','5 for result'")
    s = int(input("Enter operation: "))
    if s == 5:
        break
    y = int(input("Take another number: "))

    if s == 1:
        result = result + y
    elif s == 2:
        result = result - y
    elif s == 3:
        result = result * y
    elif s == 4:
        result = result / y
    print("Your Answeer: ", result)

print('Your answer is:',result)

# Operations: '1 for Addition','2 for Substraction','3 for Multiplication','& 4 for Division','5 for result'
# Enter operation: 2+4+10-4*5