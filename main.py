from os import system, name
import sys
import bisect
import time
from colorama import Fore, Back, Style

# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

class Cell:
    def __init__ (self,x,y,weight, prec = None):
        self.x = x
        self.y = y
        self.w = weight
        self.prec = prec
    def __lt__(self, other):
        return self.w < other.w
    def __repr__(self):
            return 'Cell({},{});'.format(self.x, self.y)
    def near(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) < 2
    def same(self, x, y):
        return self.x == x and self.y == y

def findStartEnd(inp):
    for i in range(0,len(inp)):
        for j in range(0,len(inp[i])):
            if inp[i][j] == "s":
                s = (j, i)
            elif inp[i][j] == "f":
                f = (j, i)
    return(s,f)

def measureWeight(s, f, x, y):
    return abs(s[0] - x) + abs(s[1] - y) + abs(f[0] - x) + abs(f[1] - y)

def existInside(inp, x, y):
    if inp == None:
        return False
    for e in inp:
        if e.same(x,y):
            return True
    return False

def insertQuestion(inp, ext, x, y):
    for e in ext:
        if e.same(x,y):
            return False
    for e in inp:
        if e.same(x,y):
            return False
    return True

def printalo(inp, todo, done, path = None):
    clear()
    for y in range(0, len(inp)):
        for x in range(0, len(inp[y])):
            if inp[y][x] == 's' or inp[y][x] == 'f':
                print(Back.CYAN, end = '')
            if existInside(todo, x, y):
                print(Back.YELLOW, end = '')
            if existInside(done, x, y):
                print(Back.WHITE, end = '')
            if existInside(path, x, y):
                print(Back.GREEN, end = '')
            print(inp[y][x], end = '')
            print(Style.RESET_ALL, end = '')
        print()
    print(Style.RESET_ALL, end = '')

if __name__ == "__main__":
    with open("inputs/" + sys.argv[1]+".txt") as f:
        inp = f.read().splitlines()
    #ordered array
    todo = list()
    #cells yet done
    done = list()
    s,f = findStartEnd(inp)
    todo.append(Cell(*s, measureWeight(s, f, *s)))
    #start -> look near cells chose 1 and add the others to todo list
    while True:
        if len(todo) == 0:
            print("no path found")
            break
        look = todo.pop(0)
        if inp[look.y][look.x] == 'f':
            print("found path")
            a = list()
            while look != None:
                a.append(look)
                look = look.prec
            printalo(inp, todo, done, a)
            break
        if look not in done:
            done.append(look)
            #check left
            if look.x - 1 >= 0 and inp[look.y][look.x - 1] != "x" and insertQuestion(todo, done, look.x - 1, look.y):
                bisect.insort_left(todo, Cell(look.x - 1, look.y, measureWeight(s, f, look.x - 1, look.y), look))
            #check right
            if look.x + 1 < len(inp[look.y]) and inp[look.y][look.x + 1] != "x" and insertQuestion(todo, done, look.x + 1, look.y):
                bisect.insort_left(todo, Cell(look.x + 1, look.y, measureWeight(s, f, look.x + 1, look.y), look))
            #check up
            if look.y - 1 >= 0 and inp[look.y - 1][look.x] != "x" and insertQuestion(todo, done, look.x, look.y - 1):
                bisect.insort_left(todo, Cell(look.x, look.y - 1, measureWeight(s, f, look.x, look.y - 1), look))
            #check down
            if look.y + 1 < len(inp) and inp[look.y + 1][look.x] != "x" and insertQuestion(todo, done, look.x, look.y + 1):
                bisect.insort_left(todo, Cell(look.x, look.y + 1, measureWeight(s, f, look.x, look.y + 1), look))
        if len(sys.argv) > 2 and sys.argv[2] == "-d":
            printalo(inp, todo, done)
            time.sleep(0.01)