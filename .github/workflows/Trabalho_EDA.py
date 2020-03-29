import numpy as np
class NQueens:
    
    def __init__(self):
        self.__size = 0
        self.__solutions = 0

    def size(self,size):
        self.__solutions = 0
        self.__size = size
        print("O tabuleiro é de",self.__size,"por",self.__size)

    def check_size(self):
        if self.__size==0:
            print("Tem de atribuir um valor usando a função size()")
        else:
            print("O tabuleiro é de",self.__size,"por",self.__size)

    def matriz(self):
        self.__size= np.zeros([self.__size,self.__size])

    def place_n_queens(self, positions, target):
        if target == self.__size:
            self.__solutions += 1
        else:
            column = 0
            while column != self.__size:
                column +=1
                if self.unguarded(positions, target, column):
                    positions[target] = column
                    self.place_n_queens(positions, target + 1)

    def unguarded(self, positions, target, column):
        for i in range(target):
            if positions[i] == column or positions[i] - i == column - target or positions[i] + i == column + target:
                return False
        return True

    def solve(self):
        if self.__solutions!= 0:
            print("Num Tabuleiro de",self.__size,"x",self.__size,"são possiveis",self.__solutions,"soluções")
        else:
            positions = [-1] * self.__size
            self.place_n_queens(positions, 0)
            print("Num Tabuleiro de",self.__size,"x",self.__size,"são possiveis",self.__solutions,"soluções")

    def reset(self):
        self.__size = 0
        self.__solutions = 0


