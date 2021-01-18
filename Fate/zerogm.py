import random

outcomes = [
      "uno de tus aspectos",
      "uno de tus proezas",
      "uno de tus aliados",
      "uno de tus enemigos",
      "lo que intentabas hacer",
      "el escenario donde estás",
      "un aspecto temporal beneficioso para ti",
      "un aspecto temporal perjudicial para ti",
      "tu concepto de personaje",
      "tu personaje"
    ]

fatedice = ["+", "0", "-"]

def roll_die():
    result = random.choice(fatedice)
    return result

def fate_roll():
    my_throw = []
    for i in range(0, 4):
        my_throw.append(roll_die())

    return my_throw

def check_and_generate_random_event(roll):
    pluses = 0
    minus = 0

    for result in roll:
        if result == "+":
            pluses += 1
        if result == "-":
            minus += 1

    if pluses >= 3:
        return ", y además ocurre algo positivo relacionado con " + random.choice(outcomes)
    if minus >= 3:
        return ", y además se fuerza uno de tus aspectos"

    return ""


def calculate_total(dice_results):
    total = 0
    for dice_result in dice_results:
        if dice_result == "-":
            total += -1
        if dice_result == "0":
            total += 0
        if dice_result == "+":
            total += 1
    
    return total

def set_difficulty():
    return input("Define probabilidad de -4 a 4: ")

def ask_oracle():
    difficulty = set_difficulty()
    roll = fate_roll()
    total = calculate_total(roll) + int(difficulty)
    print("Tirada:\n") 
    print(roll) 
    print("\nTotal: " + str(total))

    if total >= 0:
        print("Sí" + check_and_generate_random_event(roll))
    if total < 0:
        print("No" + check_and_generate_random_event(roll))

while 1:
    ask_oracle()