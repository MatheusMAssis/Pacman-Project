import time

class Pacman:
    
    def __init__(self):
        self.pos = PVector(13*16 + 8, 23*16 + 8)
        self.vel = PVector(-1, 0)
        self.dir = PVector(-1, 0)
        self.turn = False
        self.win = False
        self.score = 0
  
    def draw_pacman(self):
        noStroke()
        fill(255, 235, 5)
        ellipse(self.pos.x, self.pos.y, 20, 20)
    
    def move(self, table):
        if self.turn:
            self.pos.add(self.vel)
            
    def check_win(self):
        if self.score == 246:
            self.win = True
    
    def check_position(self, table, ghost):
        
        #--- if on critical position ---#
        
        if ((self.pos.x - 8) % 16 == 0 and (self.pos.y - 8) % 16 == 0):
            m_pos = PVector((self.pos.x - 8) / 16, (self.pos.y - 8) / 16)
            if not table[floor(m_pos.y)][floor(m_pos.x)].eaten:
                table[floor(m_pos.y)][floor(m_pos.x)].eaten = True
                self.score += 1
                if table[floor(m_pos.y)][floor(m_pos.x)].big_dot:
                    t0 = time.time()
                    while time.time() - t0 <= 10:
                        ghost.vulnerable()
                    ghost.r, ghost.b = 255, 0
                
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
            if (self.pos.x + 10 * self.vel.x - 8) % 16 == 0 and (self.pos.y + 10 * self.vel.y - 8) % 16 == 0:
                m_pos = PVector((self.pos.x + 10 * self.vel.x - 8) / 16, (self.pos.y + 10 * self.vel.y - 8) / 16)
                if not table[floor(m_pos.y)][floor(m_pos.x)].eaten:
                    table[floor(m_pos.y)][floor(m_pos.x)].eaten = True
                    self.score += 1
                    if table[floor(m_pos.y)][floor(m_pos.x)].big_dot:
                        t0 = time.time()
                        while time.time() - t0 <= 10:
                            ghost.vulnerable()
                        ghost.r, ghost.b = 255, 0
                        
                    
            if self.dir.x + self.vel.x == 0 and self.dir.y + self.vel.y == 0:
                self.vel = PVector(self.dir.x, self.dir.y)
                self.turn = True
                return True
            self.turn = True
            return True
