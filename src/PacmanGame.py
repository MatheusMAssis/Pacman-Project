import Pacman as p
import Map as m
import Ghost as g

pacman = p.Pacman()
ghost = g.Ghost()
start_game = False

#--- map representation ---#

table = [[0 for i in range(28)] for j in range(31)]
table_representation = \
[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 1, 1, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 1], 
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1], 
[1, 8, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 8, 1], 
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1], 
[1, 4, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 4, 1], 
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1], 
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1], 
[1, 4, 0, 0, 0, 0, 4, 1, 1, 4, 0, 0, 4, 1, 1, 4, 0, 0, 4, 1, 1, 4, 0, 0, 0, 0, 4, 1], 
[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 6, 1, 1, 6, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 6, 1, 1, 6, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 0, 1, 1, 5, 6, 6, 5, 6, 6, 5, 6, 6, 5, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 0, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 0, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 4, 6, 6, 5, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 4, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 0, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 0, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 0, 1, 1, 5, 6, 6, 6, 6, 6, 6, 6, 6, 5, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 0, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 0, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
[1, 4, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 4, 1, 1, 4, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 4, 1], 
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1], 
[1, 8, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 8, 1], 
[1, 4, 0, 4, 1, 1, 4, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 4, 1, 1, 4, 0, 4, 1], 
[1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1], 
[1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1], 
[1, 4, 0, 4, 0, 0, 4, 1, 1, 4, 0, 0, 4, 1, 1, 4, 0, 0, 4, 1, 1, 4, 0, 0, 4, 0, 4, 1], 
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], 
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], 
[1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#--- game code ---#

def setup():
    frameRate(100)
    size(448, 496)
    
    
    for i in range(28):
        for j in range(31):
            table[j][i] = m.Map(16*i+8, 16*j+8)
            if table_representation[j][i] == 1:
                table[j][i].wall = True
            elif table_representation[j][i] == 0 or table_representation[j][i] == 4:
                table[j][i].small_dot = True
            elif table_representation[j][i] == 8:
                table[j][i].big_dot = True
            elif table_representation[j][i] == 6 or table_representation[j][i] == 5:
                table[j][i].eaten = True
            
def draw():
    global pacman, start_game
            
    #--- home screen ---#
    
    if not start_game:
        background(0)
        fill(255)
        textAlign(CENTER)
        textSize(40)
        text('PACMAN', width/2, height/2)
        textSize(14)
        text('version 1.0', width/2, height/2 + 20)
        textSize(20)
        text('CLICK TO START', width/2, height - 50)
        textSize(10)
        text('developed by: Matheus de Moncada Assis', width/2, 20)
            
    #--- game itself ---#
    
    else:
        img = loadImage("map.jpg")
        background(img)
        
        
        #--- drawing pacman and map ---#
        
        for i in range(28):
            for j in range(31):
                table[j][i].draw_dot()
                
        pacman.draw_pacman()
        ghost.draw_ghost(ghost.r, ghost.g, ghost.b)
        
        #--- moving and checking pacman ---#
        
        pacman.check_position(table, ghost)
        pacman.move(table)
        pacman.check_win()
        if pacman.win:
            print('YOU WIN')
        
        ghost.movement(table_representation, pacman)
        ghost.check_position(table)
        ghost.move()
        
        #--- testing if pacman was eaten by ghost ---#
        
        if dist(pacman.pos.x, pacman.pos.y, ghost.pos.x, ghost.pos.y) <= 16:
            fill(255,255,255,200)
            rect(0,0,width,height)
            textSize(40)
            fill(0)
            textAlign(CENTER)
            text('GAME OVER', width/2, height/2)
            textSize(20)
            noLoop()

    #--- command to start the game ---#
    
    if mousePressed:
        if mouseX < width and mouseY < height:
            start_game = True

#--- movement for pacman ---#

def keyPressed():
    if key == CODED:
        if keyCode == UP:
            pacman.dir = PVector(0, -1)
            pacman.turn = True
        elif keyCode == DOWN:
            pacman.dir = PVector(0, 1)
            pacman.turn = True
        elif keyCode == LEFT:
            pacman.dir = PVector(-1, 0)
            pacman.turn = True
        elif keyCode == RIGHT:
            pacman.dir = PVector(1, 0)
            pacman.turn = True
