dial = 50

password = 0

def rotate(direction, amount):
    global dial, password
    if direction == "R":
        while amount > 0:
            dial += 1

            if dial == 0:
                password += 1

            if dial > 99:
                dial = 0
                password += 1
            amount -= 1

    elif direction == "L":
        while amount > 0:
            dial -= 1

            if dial == 0:
                password += 1

            if dial < 0:
                dial = 99

            amount -= 1


with open("1_december/december1_input.txt") as file:
    for line in file:
        direction = line[0]
        amount = int(line[1:].strip())
        print(f"Rotating {direction} by {amount} from {dial}")
        rotate(direction, amount)


print(f"PASSWORD: {password}")