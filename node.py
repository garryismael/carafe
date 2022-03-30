class Noeud:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def depart(self) -> bool:
        return (self.x == 0 and self.y == 0)

    def equals(self, noeud) -> bool:
        return self.x == noeud.x and self.y == noeud.y

    def __str__(self) -> str:
        return "(%d, %d)" % (self.x, self.y)
