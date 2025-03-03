
#TASK1
a = 10
b = 5
sum = a + b
difference = a - b
product = a * b
quotient = a/b

print ("sum value is:", sum)
print ("diff is:", difference)
print ("product is:", product)
print("quotient is :", quotient)

#TASK2 COMPARISON OPERATORS

print(f"{a} < {b} -> {a < b}")
print(f"{a} > {b} -> {a > b}")
print(f"{a} >= {b} -> {a >= b}")
print(f"{a} >= {b} -> {a >= b}")
print(f"{a} <= {b} -> {a <= b}")
print(f"{a} == {b} -> {a == b}")
print(f"{a} != {b} -> {a != b}")

#task 3 

x = True
y = False
print(f"x and y -> {x and y}")  # Logical AND
print(f"x or y  -> {x or y}")   # Logical OR
print(f"not x   -> {not x}")    # Logical NOT
print(f"not y   -> {not y}") 

#task 4 assignment

# Step 1: Initialize the variable
total = 10

# Step 2: Use assignment operators to update total
total += 5   # Equivalent to total = total + 5
print(f"After += 5: {total}")  

total -= 3   # Equivalent to total = total - 3
print(f"After -= 3: {total}")  

total *= 2   # Equivalent to total = total * 2
print(f"After *= 2: {total}")  

total /= 4   # Equivalent to total = total / 4
print(f"After /= 4: {total}")  

# Step 3: Print the final value
print(f"Final value of total: {total}")
#task 5 bitwise
# Define two integers
a = 10  # 1010 in binary
b = 4   # 0100 in binary

# Perform bitwise operations
print(f"a & b  -> {a & b}")   # Bitwise AND
print(f"a | b  -> {a | b}")   # Bitwise OR
print(f"a ^ b  -> {a ^ b}")   # Bitwise XOR
print(f"~a     -> {~a}")      # Bitwise NOT
print(f"a << 1 -> {a << 1}")  # Left Shift (multiply by 2)
print(f"a >> 1 -> {a >> 1}")  # Right Shift (divide by 2)
