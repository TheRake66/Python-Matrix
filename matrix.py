from random import randint
from time import sleep
from os import system

from color import Color



class Matrix:
    
    
    
    def __init__(self,
                 fps: int = 15,
                 charset: str = "0987654321",
                 width: int = 50, 
                 height: int = 20, 
                 colors: list = [ Color.WHITE, Color.BRIGHT_GREEN, Color.BRIGHT_GREEN, Color.GREEN, Color.GREEN ],
                 luck: int = 15) -> None:
        if fps <= 0:
            raise Exception('Cannot set less than 1 fps!')
        
        if width < 5 or height < 5:
            raise Exception('Cannot set size less than 5x5!')
            
        if len(colors) == 0:
            raise Exception('You must specify clors!')
            
        if luck < 1 or luck > 100:
            raise Exception('Luck need to be between 1 and 100!')
        
        if len(charset) < 5:
            raise Exception('Cannot set chartset less than 5!')
        
        self.__fps = fps
        self.__charset = charset
        self.__width = width
        self.__height = height
        self.__colors = colors
        self.__luck = luck
        self.__matrix = [[ False for x in range(self.__width) ] 
                         for y in range(self.__height) ]
        self.__frame = None
        self.__bounds = height - 1
        self.__nbcolors = len(colors)
        self.__charmax = len(charset) - 1
        self.__running = False
        self.__time = 1 / fps
    
    
    
    def __createTears(self) -> None:
        for x in range(self.__width):
            if randint(1, 100) < self.__luck:
                self.__matrix[0][x] = True


                
    def __moveTears(self) -> None:
        for y in range(self.__bounds, -1, -1):
            for x in range(self.__width):
                if self.__matrix[y][x]:
                    self.__matrix[y][x] = False
                    if y < self.__bounds:
                        self.__matrix[y + 1][x] = True



    def __drawTears(self) -> None:
        self.__frame = [[ -1 for x in range(self.__width) ] 
                 for y in range(self.__height) ]
        
        for y in range(self.__bounds, -1, -1):
            for x in range(self.__width):
                if self.__matrix[y][x]:
                    for i in range(self.__nbcolors):
                        flow = y - i
                        if flow < 0: break
                        self.__frame[flow][x] = i



    def __printTears(self) -> None:
        for y in range(self.__height):
            for x in range(self.__width):
                value = self.__frame[y][x]
                if value > -1 :
                    char = self.__charset[randint(0, self.__charmax)]
                    color = self.__colors[value]
                    print(f'{Color.BG_BLACK}{color}{char}', end='')
                else:
                    print(f'{Color.BG_BLACK} ', end='')
            print()
        


    def stopAnimate(self) -> None:
        self.__running = False



    def startAnimate(self) -> None:
        self.__running = True
        
        while self.__running:
            self.__moveTears()
            self.__createTears()
            self.__drawTears()
            self.__printTears()
            sleep(self.__time)
            system('clear')