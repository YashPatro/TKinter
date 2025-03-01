# 1
squares = [x**2 for x in range(1, 11)]

# 2
words = ["apple", "banana", "cherry", "date", "elephant"]
word_lengths = [len(word) for word in words]

# 3
lowercase_letters = [chr(x) for x in range(97, 123)]

# 4
transformed_numbers = [x**2 if x % 2 == 0 else x**3 for x in range(-5, 6)]

# 5
first_characters = [word[0] for word in words]

# Print results
print("1. Squares from 1 to 10:", squares)
print("2. Lengths of words:", word_lengths)
print("3. Lowercase letters:", lowercase_letters)
print("4. Squares (even) & Cubes (odd) from -5 to 5:", transformed_numbers)
print("5. First characters from words:", first_characters)
