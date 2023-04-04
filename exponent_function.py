def exponent(a, b):
    k = 0
    result = 1
    while k < b:
        result = result * a
        k += 1

    return result


base = int(input("Enter base:"))
exp = int(input("Enter exponent:"))
print("The result is:", exponent(base, exp))
