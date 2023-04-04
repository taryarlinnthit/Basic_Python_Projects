i, j = 0, 0
Storage = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("-------------------------------------------------------------------------------------------------------")
print("The maximum amount is 10")
print("Please enter the amount of elements you'd like to use")
amount = int(input("Enter: "))

print("Now start entering!")
while i < amount:
    Storage[i] = int(input("Enter: "))
    i += 1
print("So the number you entered are")
while j < i:
    print(Storage[j])
    j += 1

k = 0
largest = Storage[0]

while k < amount:
    if Storage[k] > largest:
        largest = Storage[k]
    k += 1

print("The largest number is", largest)

s = 0
smallest = Storage[0]

while s < amount:
    if Storage[s] < smallest:
        smallest = Storage[s]
    s += 1
print("The smallest number is ", smallest)





