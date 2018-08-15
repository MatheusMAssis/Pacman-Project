class Ghost:
    
    def __init__(self):
        self.pos = PVector(1*16 + 8, 1*16 + 8)
        self.vel = PVector(1, 0)
        self.dir = PVector(1, 0)
        self.turn = True
    
    #--- drawing ghost ---#
    
    def draw_ghost(self):
        noStroke()
        fill(255,0,0)
        ellipse(self.pos.x, self.pos.y, 20, 20)
    
    #--- defining movements and restrictions for ghost ---#
    
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
        
        #--- else ---#
        
        else:
            if self.dir.x + self.vel.x == 0 and self.dir.y + self.vel.y == 0:
                self.vel = PVector(self.dir.x, self.dir.y)
                self.turn = True
                return True
            self.turn = True
            return True
        
    #--- using some method to make ghost move ---#
    #at this moment, it is a little bit retarded
    
    def movement(self):
        if not self.turn:
            self.dir *= -1
            self.turn = True
