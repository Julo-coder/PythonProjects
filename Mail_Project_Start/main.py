with open("./Input/Letters/starting_letter.txt", mode="r") as f:
    starting_letter = f.read()
    
with open("./Input/Names/invited_names.txt") as d:
    names = d.read().split()

for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as f:
        new_letter = starting_letter.replace("[name]", f"{name}")
        f.write(new_letter)