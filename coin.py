import random

print("Tossing a coin...")

heads = 0
tails = 0

for i in range(3):
    result = random.choice(["Heads", "Tails"])
    print(f"Round {i + 1}: {result}")
    if result == "Heads":
        heads += 1
    else:
        tails += 1

print(f"Heads: {heads}, Tails: {tails}")