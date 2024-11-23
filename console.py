import os


class Console:
    """Class to manage console.
    """
    
    
    """str: Command to clear console depending on the OS.
    """
    __clear = 'cls' if os.name == 'nt' else 'clear'
    
    
    @classmethod
    def clearAll(cls) -> None:
        """Clear console output.
        """
        os.system(cls.__clear)
    
    
    @classmethod
    def moveTo(cls, x: int, y: int) -> None:
        """Move cursor to position.

        Arguments:
            x (int): Column index.
            y (int): Row index.
        """
        print("\033[%d;%dH" % (x, y))