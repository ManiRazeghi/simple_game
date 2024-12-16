from random import randint

pc = randint(1, 100)
print(pc)
while (ask := int(input('guss number: '))) != pc:
    ask

print('good job!')