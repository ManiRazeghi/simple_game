from random import randint

pc = randint(1, 100)
guss_count = 0


while (ask := int(input('guss number: '))) != pc:

    if ask > pc:
        print('your guss is upper!')
    
    else:
        print('your guss is lower!')
    
    guss_count += 1
    
    ask

print(f'good job! your guss count is: {guss_count}')