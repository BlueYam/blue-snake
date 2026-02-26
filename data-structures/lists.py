# --- 1. Creation ---
print("\n--- CREATION SECTION ---")
# Traditional way vs. Multiplication trick
fruits = ["apple", "cherry", "banana", "apricots"]
zeros = [0] * 5  # Result: [0, 0, 0, 0, 0
print(zeros)
print(f"INITIAL FRUITS LIST: {fruits}")

# --- 2. Adding ---
print("\n--- ADDING SECTION ---")
fruits.append("date")          # Adds to the end
fruits.insert(1, "blueberry")  # Inserts at index 1
extra_fruits = ["elderberry", "fig"]
fruits += extra_fruits         # The '+' operator combines lists
print(f"CURRENT LIST AFTER ADDITIONS: {fruits}")

# --- 3. Deleting with Style ---
print("\n--- DELETING SECTION ---")
del fruits[0]                  # Removes by index
fruits.remove("banana")        # Removes by value
last_item = fruits.pop()       # "Pops" the last item out and returns it
print(f"CURRENT LIST AFTER DELETION: {fruits}")


# --- 5. The "Copy" Trap ---
print("\n--- COPY SECTION ---")
# WRONG: list_b = list_a (This just points to the same list!)
# RIGHT: 
list_a = [1, 2, 3]
list_b = list_a[:]  # Or list_a.copy()
list_c = list_b.copy() + [4, 5, 6]
print(list_a)
print(list_b)
print(list_c)

# --- 6. Slicing ---
print("\n--- SLICING SECTION ---")
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:5])    # [2, 3, 4] (Stop is exclusive)
print(nums[:3])     # [0, 1, 2] (From beginning)
print(nums[::2])    # [0, 2, 4, 6, 8] (Every second element)
print(nums[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (Easy reverse!)

# --- 7. Searching and Sorting ---
print("\n--- SEARCHING AND SORTING SECTION ---")
if "cherry" in fruits:
    print(f"Found cherry at index: {fruits.index('cherry')}")

fruits.sort()                  # Sorts the list alphabetically/numerically
print(f"SORTED BY ALPHA: {fruits}")
fruits.reverse()               # Flips the order
print(f"REVERSED: {fruits}")
print(f"LENGTH OF LIST: {len(fruits)}") # Length/Size of list
print(f"APRICOT FREQUENCY: {fruits.count('apricot')}")
print(f"SUM OF LIST: {sum(nums)}") # Sum of all numbers
print(f"MAX: {max(nums)} MINS: {min(nums)}") # Get maximum and minimum

# --- 8. List comprehension ---
print("\n--- LIST COMPREHENSION SECTION ---")
# Traditional way
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)
    

# List Comprehension way
comprehension_squares = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]
print(comprehension_squares)

# With a filter (if statement)
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)