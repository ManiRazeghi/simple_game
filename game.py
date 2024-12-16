from random import randint

pc = randint(1, 100)
guss_count = 0
heart = int(input('heart: ')


while (ask := int(input('guss number: '))) != pc:

    if ask > pc:
        print('your guss is upper!')
    
    else:
        print('your guss is lower!')
    
    guss_count += 1
    heart -= 1

    if heart == 0:
        print(f'game over! answer: {pc}')
        break
    
    ask

print(f'your guss count is: {guss_count}')
