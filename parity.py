# A function that takes a number and returns "Even" or "Odd"
def parity_label(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test
print(parity_label(8))  # Even
print(parity_label(9))  # Odd
