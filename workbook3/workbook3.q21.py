num = int(input("Enter a number: "))
original = num
reversed_num = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

# Preserve sign for comparison
if original < 0:
    print(f"{original} is not a palindrome (negative numbers aren't palindromes).")
elif original == reversed_num:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")
