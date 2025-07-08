def add(A,B):
    return A+B
def sub(A,B):
    return A-B
def mul(A,B):
    return A*B
def div(A,B):
    return A/B
def pow(A,B):
    return A**B

A = int(input("Enter the first number "))
B = int(input("Enter the second number "))
operation = int(input("Enter the operation you need"))

if operation == 1:
    print(add(A,B))

elif operation == 2:
    print(sub(A,B))

elif operation == 3:
    print(mul(A,B))

elif operation == 4:
    print(div(A,B))

elif operation == 5:
    print(pow(A,B))

else:
    print("Retry Again!!!")