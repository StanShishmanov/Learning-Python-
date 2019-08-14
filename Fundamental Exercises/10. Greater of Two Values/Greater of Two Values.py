type = input()

if type == "int":
    a = int(input())
    b = int(input())
    print(max(a,b))
elif type == "char":
    a = input()
    b = input()
    print(max(a, b))
elif type == "string":
    a = input()
    b = input()
    if a > b:
        print(a)
    else:
        print(b)