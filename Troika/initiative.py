import random

def initiative(tokens):
    total = 0
    flatenedTokens = []

    for key, value in tokens.items():
        if value > 0:
            for i in range(0, value):
                flatenedTokens.append(key)

    if len(flatenedTokens) <= 0:
        print("No tokens")
        return

    pickindex = random.randint(1, len(flatenedTokens))
    pick = flatenedTokens[pickindex-1]
    print(tokens)
    print(pick)
    tokens[pick] -= 1
