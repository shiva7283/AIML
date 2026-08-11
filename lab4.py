# Candidate Elimination Algorithm
# Experiment: Implementation of Candidate Elimination Algorithm

# Training Dataset
data = [
    ["Sunny", "Warm", "Normal", "Strong", "Yes"],   # D1
    ["Sunny", "Warm", "High", "Strong", "Yes"],     # D2
    ["Rainy", "Cold", "High", "Strong", "No"],      # D3
    ["Sunny", "Warm", "High", "Weak", "Yes"]        # D4
]

attributes = ["Sky", "AirTemp", "Humidity", "Wind"]

# Get all possible values for each attribute
domains = []
for i in range(len(attributes)):
    domains.append(set(row[i] for row in data))


# Check whether hypothesis covers an instance
def covers(h, instance):
    for i in range(len(h)):
        if h[i] != "?" and h[i] != instance[i]:
            return False
    return True


# Check whether hypothesis is more general than another hypothesis
def more_general_or_equal(h1, h2):
    for i in range(len(h1)):
        if h1[i] != "?" and h1[i] != h2[i]:
            return False
    return True


# Remove duplicate hypotheses
def remove_duplicates(hypotheses):
    result = []
    for h in hypotheses:
        if h not in result:
            result.append(h)
    return result


# Remove hypotheses that are too general/specific
def remove_redundant(S, G):
    S = [
        s for s in S
        if any(more_general_or_equal(g, s) for g in G)
    ]

    G = [
        g for g in G
        if any(more_general_or_equal(g, s) for s in S)
    ]

    return remove_duplicates(S), remove_duplicates(G)


# Minimal generalization of a specific hypothesis
def generalize_S(s, instance):
    new_s = list(s)

    for i in range(len(s)):
        if s[i] == "∅":
            new_s[i] = instance[i]
        elif s[i] != instance[i]:
            new_s[i] = "?"

    return new_s


# Minimal specializations of a general hypothesis
def specialize_G(g, instance):
    specializations = []

    for i in range(len(g)):
        if g[i] == "?":
            for value in domains[i]:
                if value != instance[i]:
                    new_g = list(g)
                    new_g[i] = value
                    specializations.append(new_g)

    return specializations


# Print boundaries
def print_boundary(name, boundary):
    print(name)

    if not boundary:
        print("  {}")
    else:
        for h in boundary:
            print(" ", h)


# ---------------------------------------------------------
# Candidate Elimination Algorithm
# ---------------------------------------------------------

# Most Specific Boundary (S)
S = [["∅", "∅", "∅", "∅"]]

# Most General Boundary (G)
G = [["?", "?", "?", "?"]]

print("=" * 60)
print("CANDIDATE ELIMINATION ALGORITHM")
print("=" * 60)

print("\nInitial Boundaries:")
print_boundary("S (Most Specific):", S)
print_boundary("G (Most General):", G)


# Process every training instance
for step, instance in enumerate(data, start=1):

    x = instance[:-1]
    target = instance[-1]

    print("\n" + "-" * 60)
    print(f"Processing D{step}: {instance}")
    print("-" * 60)

    if target == "Yes":

        # ---------------------------------------------
        # Positive Example
        # ---------------------------------------------

        # Remove G hypotheses that do not cover x
        G = [g for g in G if covers(g, x)]

        new_S = []

        for s in S:

            if covers(s, x):
                new_S.append(s)

            else:
                generalized = generalize_S(s, x)

                # Keep only if there exists a G that is
                # more general than the new S
                for h in [generalized]:
                    if any(more_general_or_equal(g, h) for g in G):
                        new_S.append(h)

        S = remove_duplicates(new_S)

    else:

        # ---------------------------------------------
        # Negative Example
        # ---------------------------------------------

        # Remove S hypotheses that cover the negative example
        S = [s for s in S if not covers(s, x)]

        new_G = []

        for g in G:

            if not covers(g, x):
                new_G.append(g)

            else:
                specializations = specialize_G(g, x)

                # Keep specializations that are more general
                # than at least one member of S
                for h in specializations:
                    if any(more_general_or_equal(h, s) for s in S):
                        new_G.append(h)

        G = remove_duplicates(new_G)

    # Remove inconsistent/redundant hypotheses
    S, G = remove_redundant(S, G)

    print(f"\nAfter processing D{step}:")
    print_boundary("S (Specific Boundary):", S)
    print_boundary("G (General Boundary):", G)


# ---------------------------------------------------------
# Final Version Space
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("FINAL VERSION SPACE BOUNDARIES")
print("=" * 60)

print_boundary("S (Most Specific Boundary):", S)
print_boundary("G (Most General Boundary):", G)

print("\nCandidate Elimination completed successfully.")