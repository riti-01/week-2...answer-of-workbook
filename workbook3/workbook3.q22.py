a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

max_val = max(a, b)

while True:
    if max_val % a == 0 and max_val % b == 0:
        lcm = max_val
        break
    max_val += 1

print(f"The LCM of {a} and {b} is {lcm}")
