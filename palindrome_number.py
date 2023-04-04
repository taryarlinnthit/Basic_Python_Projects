number = int(input("Enter Number:"))
original_num = number
reverse_number = 0
while number > 0:
    reminder = number % 10
    reverse_number = (reverse_number * 10) + reminder
    number = number // 10

print(original_num)
print(reverse_number)

if original_num == reverse_number:
    print("Yes. given number is palindrome number")
else:
    print("No, given number isn't palindrome number")


