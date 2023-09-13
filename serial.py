"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """


    def __init__(self,start):
        """
        parameters:
        ------------
        start : int
            determines the starting number of the serial generator instance
        """
        self.start = start
        self.num = start

    def generate(self):
        """prints the current number and increments number by one"""
        print(self.num)
        self.num += 1
    
    def reset(self):
        """resets number to it's starting value"""
        self.num = self.start