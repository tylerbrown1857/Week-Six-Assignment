#A header comment with your name and the class name
#A function definition for the following functions:
import random
def populate(world,h,w):
    for x in range (h):
        row = []
        for y in range (w):
            
            row.append(random.randint(0,1))
            
        world.append(row)
    return 0

def display(world,h,w):
    worldString = ""
    for x in range(h):
        rowString = ""
        for y in range(w):
            if world[x][y] == 0: 
                rowString + " "
            else:
                rowString + "*"
                
            #rowString += world[x][y]
        worldString += rowString + "\n"
    print(worldString)
    return 0

def generation(world,h,w):
    newWorld = []
    
    n = 0
    for x in range(1,h-1):
        for y in range(1,w-1):
            n = world[x - 1][y - 1] + \
            world[x - 1][y] + \
            world[x - 1][y + 1] + \
            world[x][y - 1] + \
            world[x][y + 1] + \
            world[x + 1][y - 1] + \
            world[x + 1][y] + \
            world[x + 1][y + 1]
                
            if world[x][y] == 0:
                if n == 3:
                    newWorld[x][y] = 1
            
            else:
                if n<2 or n>3:
                    newWorld[x][y] == 0
    world = newWorld
    return 0

def main():
    world = []
    height = 22
    width = 80
    
    populate(world, height, width)
    display(world, height, width)
    
    c = input("Enter any key")
    
    while(c != 'q'):
        populate(world, height, width)
        generation(world, height, width)
        display(world, height, width)
        c = input("Enter any key")

main()