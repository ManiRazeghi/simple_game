from random import randint
import os
import time

def game(heart: int, pc) -> None:
    guss_count = 0
    
    while (ask := int(input('guss number: '))) != pc:
        
        print('your guss is upper!' if ask > pc else 'your guss is lower!')
           
        guss_count += 1
        heart -= 1

        if heart == 0:
           print(f'game over! answer: {pc}')
           break
    
        ask

    print(f'your guss count is: {guss_count}')


while (ask := input('play?(y/n): ').lower()) == 'y':
   game(int(input('heart: ')), randint(1, 100))
   ask

print('have a good day!')
time.sleep(0.5)
os.system('cls')


