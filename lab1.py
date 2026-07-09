# Generate all 4-digit PINs
# Conditions:
# 1. Digits must be even (0,2,4,6,8)
# 2. Sum of digits = 16

digits = [0, 2, 4, 6, 8]
count = 0

print("Possible PINs:\n")

for d1 in digits:
    for d2 in digits:
        for d3 in digits:
            for d4 in digits:
                if d1 + d2 + d3 + d4 == 16:
                    pin = f"{d1}{d2}{d3}{d4}"
                    print(pin)
                    count += 1

print("\nTotal possible PINs:", count)