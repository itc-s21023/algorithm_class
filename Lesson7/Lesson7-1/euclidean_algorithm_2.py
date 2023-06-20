def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

print("a≧bとなる自然数を入力してください")
a = int(input("a="))
b = int(input("b="))
print("それらの数の最大公約数は", euclid(a, b))