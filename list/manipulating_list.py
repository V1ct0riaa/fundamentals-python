# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

# Adding elements
fruits.append("orange")  # Add single element
fruits.extend(["grape", "kiwi"])  # Add multiple elements
fruits.insert(1, "mango")  # Insert at specific index

# Removing elements
fruits.remove("banana")  # Remove by value
removed = fruits.pop()  # Remove last element (returns it)
removed_at_index = fruits.pop(0)  # Remove at specific index

# Modifying elements
numbers[0] = 10  # Change element at index
numbers[1:3] = [20, 30]  # Slice assignment

# Sorting and reversing
numbers.sort()  # Sort in-place
numbers.reverse()  # Reverse in-place
sorted_numbers = sorted(numbers, reverse=True)  # Return new sorted list

# Searching
if "apple" in fruits:
    index = fruits.index("apple")  # Find index of element

# Copying lists
fruits_copy = fruits.copy()  # Shallow copy
numbers_copy = list(numbers)  # Another way to copy

# Clearing
fruits.clear()  # Remove all elements

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")