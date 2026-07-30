# Find-S Algorithm
import csv

# Read dataset
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

# Separate header and dataset
header = data[0]
dataset = data[1:]

print("Dataset:\n")
for row in dataset:
    print(row)

# Initialize hypothesis
hypothesis = None

print("\n========== Find-S Algorithm ==========\n")

step = 1

for row in dataset:

    # Last column is the target class
    if row[-1].strip().lower() == "yes":

        # Attributes only (exclude target class)
        attributes = row[:-1]

        if hypothesis is None:
            hypothesis = attributes.copy()
        else:
            for i in range(len(hypothesis)):
                if hypothesis[i] != attributes[i]:
                    hypothesis[i] = "?"

    print(f"Step {step}: {hypothesis}")
    step += 1

print("\n======================================")
print("Final Most Specific Hypothesis:\n")
print(hypothesis)