total = 0

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    total += num

average = total / 10
print("The average is:", average)
