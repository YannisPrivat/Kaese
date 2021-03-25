class Brett:
    

    def __init__(self, R, C):
        self.field = []
        self.ROWS = R
        self.COLUMNS = C

        for x in range(self.ROWS):
            row = []
            for y in range(self.COLUMNS):
                if (x==0 or x==(self.ROWS-1) or y==0 or y==(self.COLUMNS-1)):
                    cell = Kante(x, y, True, 0, False)
                elif ((x % 2 == 1 and y % 2 == 1) or (x % 2 == 0 and y % 2 == 0)):
                    cell = Feld(x, y, False, 0)
                else:
                    cell = Kante(x, y, True, 0, False)
                row.append(cell)
            self.field.append(row)

    def brettPrint(self):
        output = ""
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                output += str(self.field[row][column].getValue())
            output += "\n"
            
        print(output)

class Cell:

    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos

    def setX(self, val):
        self.xPos = val

    def setY(self, val):
        self.yPos = val


class Feld(Cell):
    def __init__(self, xPos, yPos, taken, belongs):
        super().__init__(xPos, yPos)
        self.taken = taken
        self.belongs = belongs
    
    def getValue(self):
        if (self.taken):
            return 1
        else:
            return 0

    def getBelongs(self):
        return self.belongs
    
    def setTaken(self):
        self.taken = True

    def setBelongs(self, player):
        self.belongs = player

class Kante(Cell):
    def __init__(self, xPos, yPos, taken, belongs, last):
        super().__init__(xPos, yPos)
        self.taken = taken
        self.belongs = belongs
        self.last = last
    
    def getValue(self):
        if (self.taken):
            return 1
        else:
            return 0

    def getBelongs(self):
        return self.belongs
    
    def isLast(self):
        return self.last

    def setTaken(self):
        self.taken = True

    def setBelongs(self, player):
        self.belongs = player

    def setLast(self, isLast):
        self.last = isLast


    

def main():
    brett = Brett(10,10)
    brett.brettPrint()

main()
    