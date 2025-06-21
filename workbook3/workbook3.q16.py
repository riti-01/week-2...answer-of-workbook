char = input("Enter a single alphabet character: ").lower()

if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet character.")
