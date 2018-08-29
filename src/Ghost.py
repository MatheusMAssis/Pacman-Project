class Ghost:
    
    def __init__(self):
        self.pos = PVector(1*16 + 8, 1*16 + 8)
        self.vel = PVector(1, 0)
        self.dir = PVector(1, 0)
        self.turn = True
        self.r = 255
        self.g = 0
        self.b = 0
        
    #--- drawing ghost ---#
    
    def draw_ghost(self, r, g, b):
        noStroke()
        fill(r, g, b)
        ellipse(self.pos.x, self.pos.y, 20, 20)

    #--- if pacman eats a big_dot ---#
    
    def vulnerable(self):
        self.r = 0
        value = random(0, 1)
        if value <= 0.5:
            self.b = 0
        else:
            self.b = 255
    
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
    
    #--- changing direction ---#

        
    
    
    #--- using some method to make ghost move ---#
    
    def movement(self, table, target):
        if ((self.pos.x - 8) % 16 == 0 and (self.pos.y - 8) % 16 == 0):
            m_pos = PVector((self.pos.x - 8) / 16, (self.pos.y - 8) / 16)
            if table[floor(m_pos.y)][floor(m_pos.x)] == 4 or table[floor(m_pos.y)][floor(m_pos.x)] == 5:
                vect = PVector(self.pos.x - target.pos.x, self.pos.y - target.pos.y)
                max_pos = max(abs(vect.x), abs(vect.y))
                if max_pos == abs(vect.x):
                    if self.turn:
                        if max_pos == vect.x:
                            if self.dir != PVector(1, 0):
                                self.dir = PVector(-1, 0)
                                self.turn = True
                        else:
                            if self.dir != PVector(-1, 0):
                                self.dir = PVector(1, 0)
                                self.turn = True
                    
                                            
                    #--- testing ---#
                    
                    
                    else:
                        if table[floor(m_pos.y) - 1][floor(m_pos.x)] == 1:
                            if max_pos == vect.x:
                                self.dir = PVector(0, -1)
                                self.turn = True
                            else:
                                self.dir = PVector(0, 1)
                                self.turn = True
                        elif table[floor(m_pos.y) + 1][floor(m_pos.x)] == 1:
                            if max_pos == vect.x:
                                self.dir = PVector(0, 1)
                                self.turn = True
                            else:
                                self.dir = PVector(0, -1)
                                self.turn = True
                        else:
                            self.dir = PVector(0, 1)
                            self.turn = True
                        
                else:
                    if self.turn:
                        if max_pos == vect.y:
                            if self.dir != PVector(0, 1):
                                self.dir = PVector(0, -1)
                                self.turn = True
                        else:
                            if self.dir != PVector(0, -1):
                                self.dir = PVector(0, 1)
                                self.turn = True
                    
                    
                    #--- testing ---#
                    
                    
                    else:
                        if table[floor(m_pos.y)][floor(m_pos.x) - 1] == 1:
                            if max_pos == vect.x:
                                print('aqui3')
                                self.dir = PVector(-1, 0)
                                self.turn = True
                            else:
                                self.dir = PVector(1, 0)
                                self.turn = True
                        elif table[floor(m_pos.y)][floor(m_pos.x) + 1] == 1:
                            if max_pos == vect.x:
                                self.dir = PVector(1, 0)
                                self.turn = True
                            else:
                                self.dir = PVector(-1, 0)
                                self.turn = True
                        else:
                            self.dir = PVector(1, 0)
                            self.turn = True
