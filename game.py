from random import randint

def game(heart: int, pc) -> None:
    guss_count = 0
    
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


while (ask := input('play?(y/n): ')) == 'y':
   game(int(input('heart: ')), randint(1, 100))
   ask


