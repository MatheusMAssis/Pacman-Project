class Map:
    
    def __init__(self, x, y):
        self.wall = False
        self.small_dot = False
        self.big_dot = False
        self.eaten = False
        self.x = x
        self.y = y
    
    #--- drawing on map ---#
    
    def draw_dot(self):
        if self.small_dot:
            if not self.eaten:
                fill(255, 255, 0)
                noStroke()
                ellipse(self.x, self.y, 3, 3)
                
        elif self.big_dot:
            if not self.eaten:
                fill(255, 255, 0)
                noStroke()
                ellipse(self.x, self.y, 6, 6)
