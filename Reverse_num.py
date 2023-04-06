i, j = 1, 1
print("Enter the amount of elements:")
amount = int(input("Enter:"))
storage = []

while i <= amount:
    storage.append(input("{}Enter:".format(i)))
    i += 1

print("The reverse is:")
while j <= amount:
    print(storage[amount - j])
    j += 1
