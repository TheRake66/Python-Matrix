from random import randint
import time

from color import Color
from console import Console


class Matrix:
    """Class of the Matrix animation.
    """
    

    def __init__(self,
                 fps: int = 15,
                 charset: str = '1234567890',
                 width: int = 50, 
                 height: int = 15, 
                 colors: list = [ Color.WHITE, Color.BRIGHT_GREEN, Color.BRIGHT_GREEN, Color.GREEN, Color.GREEN ],
                 luck: int = 10) -> None:
        """Constructor of class.

        Arguments:
            fps (int, optional): Frames per second. Defaults to 15.
            charset (str, optional): Characters set. Defaults to '1234567890'.
            width (int, optional): Number of columns. Defaults to 50.
            height (int, optional): Number of rows. Defaults to 15.
            colors (list, optional): List of colors. Defaults to [ Color.WHITE, Color.BRIGHT_GREEN, Color.BRIGHT_GREEN, Color.GREEN, Color.GREEN ].
            luck (int, optional): Luck to create tears on each frame. Defaults to 10.

        Raises:
            Exception: If "fps" argument is less than 1.
            Exception: If "width" or "height" arguments are less than 5.
            Exception: If "colors" argument is empty.
            Exception: If "luck" argument is not in range 1 to 100.
            Exception: If "charset" argument is empty.
        """
        if fps < 1:
            raise Exception('Cannot set less than 1 fps!')
        
        if width < 5 or height < 5:
            raise Exception('Cannot set size less than 5x5!')
            
        if colors == []:
            raise Exception('You must specify colors!')
            
        if luck < 1 or luck > 100:
            raise Exception('Luck need to be between 1 and 100!')
        
        if charset == '':
            raise Exception('You must specify charset!')
        
        self.__charset = charset
        self.__width = width
        self.__height = height
        self.__colors = colors
        self.__luck = luck
        self.__matrix = [[ -1 for x in range(self.__width) ] 
                         for y in range(self.__height) ]
        self.__frame = ''
        self.__heightmax = height - 1
        self.__colormax = len(colors) - 1
        self.__charmax = len(charset) - 1
        self.__running = False
        self.__tick = 1 / fps
    
    
    def __createTears(self) -> None:
        """Create tears on first row.
        """
        for x in range(self.__width):
            if randint(1, 100) <= self.__luck:
                self.__matrix[0][x] = 0
                
                
    def __moveTears(self) -> None:
        """Move all tears to next row.
        """
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
        """Create frame with all tears with correct color and random character.
        """
        self.__frame = Color.BG_BLACK
        for y in range(self.__height):
            for x in range(self.__width):
                value = self.__matrix[y][x]
                if value > -1 :
                    char = self.__charset[randint(0, self.__charmax)]
                    color = self.__colors[value]
                    self.__frame += color + char
                else:
                    self.__frame += f' '
            self.__frame += '\n'
        self.__frame += Color.RESET
        

    def stopAnimate(self) -> None:
        """Stop the animation.
        """
        self.__running = False
        Console.clearAll()


    def startAnimate(self) -> None:
        """Start the animation.
        """
        self.__running = True
        Console.clearAll()
        
        while self.__running:
            start = time.time()

            self.__moveTears()
            self.__createTears()
            self.__drawTears()
            
            Console.moveTo(0, 0)
            Console.writeStd(self.__frame)
            
            end = time.time()
            stamp = end - start
            if stamp < self.__tick:
                time.sleep(self.__tick - stamp)