from random import randint
import time, os


FPS = 15
CHARSET = '1234567890'
WIDTH = 50
HEIGHT = 15
COLORS = [ '\033[37m', '\033[92m', '\033[92m', '\033[32m', '\033[32m' ]
LUCK = 10


matrix = [[ -1 for x in range(WIDTH) ] for y in range(HEIGHT) ]
HEIGHTmax = HEIGHT - 1
colormax = len(COLORS) - 1
charmax = len(CHARSET) - 1
tick = 1 / FPS
clear = 'cls' if os.name == 'nt' else 'clear'


os.system(clear)
while True:
    start = time.time()

    for y in range(HEIGHTmax, -1, -1):
        for x in range(WIDTH):
            value = matrix[y][x]
            if value > -1:                    
                if value == 0 and y < HEIGHTmax:
                    matrix[y + 1][x] = 0
                if value == colormax:
                    matrix[y][x] = -1
                else:
                    matrix[y][x] += 1

    for x in range(WIDTH):
        if randint(1, 100) <= LUCK:
            matrix[0][x] = 0
                
    frame = ''
    for y in range(HEIGHT):
        for x in range(WIDTH):
            value = matrix[y][x]
            if value > -1 :
                char = CHARSET[randint(0, charmax)]
                color = COLORS[value]
                frame += f'{color}{char}'
            else:
                frame += f' '
        frame += '\n'
    print(f'\033[0;0H\033[40m{frame}\033[0m', end='')
    
    end = time.time()
    stamp = end - start
    if stamp < tick:
        time.sleep(tick - stamp)