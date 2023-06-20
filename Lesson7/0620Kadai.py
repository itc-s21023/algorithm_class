def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

def gcd(a, b):
    return euclid(a, b)

def lcm(a, b):
    gcd_value = gcd(a, b)
    return (a * b) // gcd_value

def find_gcd(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    return result

def find_lcm(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

print("3つの自然数を入力してください")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

numbers = [a, b, c]

gcd_value = find_gcd(numbers)
lcm_value = find_lcm(numbers)

print("それらの数の最大公約数は", gcd_value)
print("それらの数の最小公約数は", gcd_value // lcm_value)
print("それらの数の最大公倍数は", lcm_value)
print("それらの数の最小公倍数は", lcm_value // gcd_value)
