import os


class Console:
    
    __clear = 'cls' if os.name == 'nt' else 'clear'
    
    
    @classmethod
    def clearAll(cls) -> None:
        os.system(cls.__clear)
    
    
    @classmethod
    def moveTo(cls, x: int, y: int) -> None:
        print("\033[%d;%dH" % (x, y))