import pygame
import sys


ROWS = 15
COLUMNS = 15
WIDTH = 720
HEIGHT = 720
CSIZE = WIDTH//(COLUMNS/2) #CELLSIZE
LSIZE = 5 #LINEWIDTH
SIZE = CSIZE + LSIZE #SIZE COMBINED


class Brett:

    def __init__(self, R, C, screen):
        self.field = []
        self.ROWS = R
        self.COLUMNS = C
        self.screen = screen

        for x in range(self.ROWS):
            row = []
            for y in range(self.COLUMNS):
                #if (x==0 or x==(self.ROWS-1) or y==0 or y==(self.COLUMNS-1)):
                #    cell = Kante(x, y, True, 0, False)
                if ((x % 2 == 1 and y % 2 == 1) or (x % 2 == 0 and y % 2 == 0)):
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


    def drawBrett(self):
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                if (self.field[row][column].getValue() == 1):
                    #if (row==0 or row == self.ROWS-1): #Erste Reihe und letzte Reihe Strich: ---
                    #    if (column % 2 == 0): 
                    #        line = pygame.Rect(CSIZE* column + LSIZE, CHEIGHT* row, CSIZE, LSIZE)
                    #        pygame.draw.rect(self.screen, (0, 0, 255), line, 0)
                    #elif (column==0 or column == self.COLUMNS-1):   #Erste und letzte Spalte Strich: |
                    #    if (row % 2 == 0):
                    #        line = pygame.Rect(CSIZE* column, CHEIGHT* row, LSIZE, CSIZE)
                    #        pygame.draw.rect(self.screen, (0, 0, 255), line, 0)
                      
                    if (row % 2 == 0):                #Gerade Y Koordinate : Strich ----
                        line = pygame.Rect((column//2 + 1)*LSIZE + (column//2) *CSIZE, (row//2 )*LSIZE + (row//2) *CSIZE, CSIZE, LSIZE)
                        pygame.draw.rect(self.screen, (0, 0, 255), line, 0)
                    elif(row % 2 == 1):                 # Ungerade Y Koordinate : Strich |
                        line = pygame.Rect((column//2 )*CSIZE + (column//2) *LSIZE, (row//2)*CSIZE + (row//2 +1) *LSIZE, LSIZE, CSIZE)
                        pygame.draw.rect(self.screen, (0, 0, 255), line, 0)




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
    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    brett = Brett(ROWS,COLUMNS, screen)
    brett.brettPrint()
    running = True
    pygame.init()

    while running:

        # Did the user click the window close button?

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False


        # Fill the background with white

        screen.fill((255, 255, 255))
        brett.drawBrett()

        # Draw a solid blue circle in the center
        #rect = pygame.Rect(100, 100, 50, 50)

        #pygame.draw.rect(screen, (0, 0, 255), rect, 3)


        # Flip the display

        pygame.display.flip()


    # Done! Time to quit.

    pygame.quit()
    sys.exit()

main()
    