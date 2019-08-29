from position import Position
from random import sample



class Labyrinthe:

    def __init__(self):

       
        self.start = None
        self.end = None
        self.hero = Position
        self.width = None
        self.height = None
        self.passages = []
        self.mur = []
        self.random_items = []

    def build(self,filename):
        

        with open(filename) as laby:
            for n_line, line in enumerate(laby):
                for n_column, c in enumerate(line):
                    position = Position(n_column, n_line)
                    if c == "S":
                        self.passages.append(position)
                        self.start = position
                    elif c == "E":
                        self.passages.append(position)
                        self.end = position
                    elif c == "P":
                        self.passages.append(position)
                        self.hero = position
                    elif c == "*":
                        self.passages.append(position)
                        self.random_items.append(position)
                    elif c == ".":
                        self.passages.append(position)
                    elif c == "#":
                        self.mur.append(position)
                    
                    
            self.width = n_column + 1
            self.height = n_line + 1
        print()


    def random_position(self):
                
                #print(sample(self.passages,k=1))
                self.random_items = sample(self.passages,k=3)
                #print(self.random_items)
   
        
    def show(self):

        
        for y in range(self.height):
            for x in range(self.width):
                position = Position(x, y)
                if position == self.start:
                    print("S",end='')
                elif position in self.random_items:
                    print("*",end='')
                elif position == self.hero:
                    print("P",end='')
                elif position == self.end:
                    print("E",end='')
                elif position in self.passages:
                    print(".",end='')
                elif position in self.mur:
                    print("#",end='')
            print()

        print('Hero',self.hero)


            


           



                        

