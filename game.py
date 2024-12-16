from random import randint

pc = randint(1, 100)


while (ask := int(input('guss number: '))) != pc:
    
    if ask > pc:
        print('your guss is upper!')
    
    else:
        print('your guss is lower!')
    
    ask

print('good job!')