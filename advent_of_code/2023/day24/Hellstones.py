class Hellstones:
    def __init__(self, sx, sy, sz, vx, vy, vz):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.vx = vx
        self.vy = vy
        self.vz = vz
        
        self.a = vy
        self.b = -vx
        self.c = vy * sx - vx * sy

    def intersects(self, hellstone):
        return self.a * hellstone.b != self.b * hellstone.a