import random as rnd

def random_birthdays(n=23):
    birthdays = []
    for i in range(n):
        birthdays.append(rnd.randint(0,364))

    return birthdays

iterations = 100000
total = 0
for i in range(iterations):
    bd = random_birthdays()
    if len(set(bd)) < len(bd): total += 1

print(total / iterations)
