import random

color_list = ["balck", "white", "blue", "yellow", "silver", "brown", "gold", "green", "red"]
animal_list = ["frog", "tiger", "panda", "bear", "lion", "duck", "goat", "cow", "horse"]
password = []

# total combos = colorlist * animallist
while len(password) < len(color_list) * len(animal_list):
    color = random.choice(color_list)
    animal = random.choice(animal_list)

    gen_pass = color + animal

    # add new combinations to password if it does not exists
    if gen_pass not in password:
        password.append(gen_pass)

# read passwords in password one by one
for gen_pass in password:
    print(gen_pass)