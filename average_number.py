a, b = 0, 0
Storage = []
total = 0
amount = int(input("Enter the amount of number:"))

while a < amount:
    Storage.append(input("{}Enter:".format(a + 1)))
    a = a + 1

while b < a:
    total = total + int(Storage[b])
    b = b + 1

average = total / amount
print("The average is ", average)
