str_x = input("Enter string:")
Object = input("Enter the word you wanna search:")

find = str_x.find(Object)
print("Finding '{}'... ".format(Object))
if find != -1:
    i = 0
    print("Found")
    count = str_x.count(Object)
    print(f"Total count of {Object} is:", count)
else:
    print("Not found")

