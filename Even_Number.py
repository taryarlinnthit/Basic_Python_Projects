i, j, k = 0, 0, 0
List = []
even_list = []
amount = int(input("Enter the amount of number:"))
while i < amount:
    List.append(int(input("{}Enter".format(i + 1))))
    i += 1

print("The numbers you entered are:")
print(List)

while j < amount:
    if (int(List[j])) % 2 == 0:
        even_list.append(int(List[j]))
        j += 1
    else:
        j += 1

if not even_list:
    print("There are no even numbers")
else:
    print("The even numbers are:")
    print(even_list)

    for number in even_list:
        k += number

    print("The total sum of the even list is:", k)


