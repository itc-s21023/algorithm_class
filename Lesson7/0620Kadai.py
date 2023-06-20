def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

def lcm(a, b):
    gcd = euclid(a, b)
    return (a * b) // gcd

def gcd_multiple_numbers(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = euclid(result, numbers[i])
    return result

def lcm_multiple_numbers(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

print("3つの自然数を入力してください")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

numbers = [a, b, c]

print("それらの数の最大公約数は", gcd_multiple_numbers(numbers))
print("それらの数の最大公倍数は", lcm_multiple_numbers(numbers))
