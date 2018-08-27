class Ghost:
    
    def __init__(self):
        self.pos = PVector(1*16 + 8, 1*16 + 8)
        self.vel = PVector(1, 0)
        self.dir = PVector(1, 0)
        self.turn = True
        self.vulnerable = False
    
    #--- if pacman eats a big_dot ---#
    #def vulnerable():
    
    #--- drawing ghost ---#
    
    def draw_ghost(self):
        t = 0
        noStroke()
        fill(255, 0, 0)
        ellipse(self.pos.x, self.pos.y, 20, 20)

    #--- defining movements and walls for ghost ---#
    
    def move(self):
        if self.turn:
            self.pos.add(self.vel)
            
    def check_position(self, table):
        
        #--- if on critical position ---#
        
        if ((self.pos.x - 8) % 16 == 0 and (self.pos.y - 8) % 16 == 0):
            m_pos = PVector((self.pos.x - 8) / 16, (self.pos.y - 8) / 16)
            if table[floor(m_pos.y + self.dir.y)][floor(m_pos.x + self.dir.x)].wall:
                if table[floor(m_pos.y + self.vel.y)][floor(m_pos.x + self.vel.x)].wall:
                    self.turn = False
                    return False
                else:
                    self.turn = True
                    return True
            else:
                self.vel = PVector(self.dir.x, self.dir.y)
                self.turn = True
                return True
        
        #--- else ---#
        
        else:
            if self.dir.x + self.vel.x == 0 and self.dir.y + self.vel.y == 0:
                self.vel = PVector(self.dir.x, self.dir.y)
                self.turn = True
                return True
            self.turn = True
            return True
        
    #--- using some method to make ghost move ---#
    
    def movement(self):
        if not self.turn:
            num = random(0, 1)
            if num <= 0.25:
                self.dir = PVector(1, 0)
            elif num <= 0.5:
                self.dir = PVector(-1, 0)
            elif num <= 0.75:
                self.dir = PVector(0, 1)
            else:
                self.dir = PVector(0, -1)
