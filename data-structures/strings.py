# --- 1. Creation ---
print("\n--- CREATION SECTION ---")
# Single, Double, and Triple quotes (for multi-line)
simple_str = "hello"
multi_line = """This is a
long string."""
# Multiplication trick works here too!
divider = "-" * 10  # Result: ----------
print(divider)
print(f"INITIAL STRING: {simple_str}")

# --- 2. "Adding" (Concatenation) ---
print("\n--- ADDING SECTION ---")
# Since strings are immutable, we create new ones
word = "Python"
word += " is cool"  # The '+' operator combines strings
prefix = "Learn "
full_sentence = prefix + word
print(f"CONCATENATED: {full_sentence}")

# --- 3. Modifying (The Transformation) ---
print("\n--- TRANSFORMATION SECTION ---")
text = "  python is fun  "
print(text.upper())  # "  PYTHON IS FUN  "
print(text.title())  # "  Python Is Fun  "
print(text.strip())  # "python is fun" (removes whitespace)
# Replace returns a NEW string
new_text = text.replace("fun", "awesome").strip()
print(f"REPLACED & STRIPPED: {new_text}")

# --- 4. Slicing ---
print("\n--- SLICING SECTION ---")
# Strings use the exact same indexing as lists!
phrase = "Character"
# [start:stop:step]
print(phrase[0:4])  # "Char" (Stop is exclusive)
print(phrase[:3])  # "Cha" (From beginning)
print(phrase[::2])  # "Caaer" (Every second char)
print(phrase[::-1])  # "retcarahC" (Easy reverse!)

# --- 5. Searching and Checking ---
print("\n--- SEARCHING SECTION ---")
sample = "The quick brown fox"
print(f"Does it start with 'The'? {sample.startswith('The')}")
print(f"Does it end with 'cat'? {sample.endswith('cat')}")

if "brown" in sample:
    print(f"Found 'brown' at index: {sample.find('brown')}")

print(f"COUNT OF 'o': {sample.count('o')}")
print(f"IS NUMERIC? {'123'.isdigit()}")  # Check if string is only numbers

# --- 6. Splitting and Joining (The Dynamic Duo) ---
print("\n--- SPLIT & JOIN SECTION ---")
csv_data = "apple,banana,cherry,date"
# .split() turns a string into a LIST
fruit_list = csv_data.split(",")
print(f"AS LIST: {fruit_list}")

# .join() turns a list into a STRING
rejoined = " | ".join(fruit_list)
print(f"REJOINED WITH PIPE: {rejoined}")

# --- 7. Formatting ---
print("\n--- FORMATTING SECTION ---")
name = "Alice"
score = 95.582
# f-strings are the modern standard
print(f"User: {name} | Score: {score:.2f}")  # .2f rounds to 2 decimals

# --- 8. The "Immutability" Trap ---
print("\n--- IMMUTABILITY SECTION ---")
msg = "Hello"
try:
    msg[0] = "J"  # This will CRASH
except TypeError:
    print("FATAL: Strings cannot be changed in place. They are permanent.")
    # Correct way:
    msg = "J" + msg[1:]
    print(f"Corrected string: {msg}")
