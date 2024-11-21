from random import randint
import time
import os

from color import Color


class Matrix:
    
    
    def __init__(self,
                 fps: int = 10,
                 charset: str = "0987654321",
                 width: int = 50, 
                 height: int = 15, 
                 colors: list = [ Color.WHITE, Color.BRIGHT_GREEN, Color.BRIGHT_GREEN, Color.GREEN, Color.GREEN ],
                 luck: int = 5) -> None:
        if fps < 1:
            raise Exception('Cannot set less than 1 fps!')
        
        if width < 5 or height < 5:
            raise Exception('Cannot set size less than 5x5!')
            
        if len(colors) == 0:
            raise Exception('You must specify clors!')
            
        if luck < 1 or luck > 100:
            raise Exception('Luck need to be between 1 and 100!')
        
        if len(charset) < 5:
            raise Exception('Cannot set chartset less than 5!')
        
        self.__charset = charset
        self.__width = width
        self.__height = height
        self.__colors = colors
        self.__luck = luck
        self.__matrix = [[ -1 for x in range(self.__width) ] 
                         for y in range(self.__height) ]
        self.__heightmax = height - 1
        self.__colormax = len(colors) - 1
        self.__charmax = len(charset) - 1
        self.__running = False
        self.__time = 1 / fps
        self.__clear = 'cls' if os.name == 'nt' else 'clear'
    
    
    def __createTears(self) -> None:
        for x in range(self.__width):
            if randint(1, 100) < self.__luck:
                self.__matrix[0][x] = 0
                
                
    def __moveTears(self) -> None:
        for y in range(self.__heightmax, -1, -1):
            for x in range(self.__width):
                value = self.__matrix[y][x]
                if value > -1:                    
                    if value == 0 and y < self.__heightmax:
                        self.__matrix[y + 1][x] = 0
                    if value == self.__colormax:
                        self.__matrix[y][x] = -1
                    else:
                        self.__matrix[y][x] += 1
                    

    def __drawTears(self) -> None:
        frame = ''
        for y in range(self.__height):
            for x in range(self.__width):
                value = self.__matrix[y][x]
                if value > -1 :
                    char = self.__charset[randint(0, self.__charmax)]
                    color = self.__colors[value]
                    frame += f'{Color.BG_BLACK}{color}{char}'
                else:
                    frame += f' '
            frame += '\n'
        print(frame)
        

    def stopAnimate(self) -> None:
        self.__running = False
        os.system(self.__clear)


    def startAnimate(self) -> None:
        self.__running = True
        
        while self.__running:
            self.__moveTears()
            self.__createTears()
            os.system(self.__clear)
            self.__drawTears()
            time.sleep(self.__time)