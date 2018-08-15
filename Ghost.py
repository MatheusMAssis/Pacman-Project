class Ghost:
    
    def __init__(self):
        self.pos = PVector(1*16 + 8, 1*16 + 8)
    
    #--- drawing ghost ---#
    
    def draw_ghost(self):
        noStroke()
        fill(255,0,0)
        ellipse(self.pos.x, self.pos.y, 20, 20)
