class Pacman:
    
    def __init__(self):
        self.x = 13*16 + 8 #initial position
        self.y = 23*16 + 8
        self.fact = 16 #"walk" factor
        self.score = 0
        self.ddx = 0 #get track of the direction
        self.ddy = 0 
        self.move = False
  
    def draw_p(self):
        noStroke()
        fill(255, 235, 5)
        ellipse(self.x, self.y, 20, 20)
    
    def direction(self, dx, dy):
        delay(30)
        
        self.move = True
        if self.move:
            self.x += dx * self.fact
            self.y += dy * self.fact
        self.ddx = dx
        self.ddy = dy
        
    def check_position(self, table):
        pos_x = (self.x - 8) / 16
        pos_y = (self.y - 8) / 16
        
        if table[pos_y][pos_x].wall:
            self.x -= self.ddx * self.fact
            self.y -= self.ddy * self.fact
        
        if ((self.x - 8) % 16 == 0 and (self.y - 8) % 16 == 0):
            if not table[pos_y][pos_x].eaten:
                table[pos_y][pos_x].eaten = True
                self.score += 1
