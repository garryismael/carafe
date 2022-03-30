from typing import List
from node import Noeud


class Tree:
    """
        racine: Predecesseur pour permettre de trouver le chemin depuis (0, 0)
        carafe: Noeud contenant la racine

        Representation:
                  [(x, y)]
       [(x1,x2)]----  |  ----[(x2, y2)]
                      .
                      .
                      .
                      |
                    [xi, yi]
    """

    def __init__(self, data: Noeud):
        self.racine: Tree = None
        self.noeud: Noeud = data
        self.successeurs: List[Tree] = []

    def insert(self, noeud: Noeud, successeurs):
        for item_succ in self.successeurs:
            if item_succ.noeud.equals(noeud):
                if len(item_succ.successeurs) < 0:
                    item_succ.successeurs.append(Tree(noeud))
                else:
                    item_succ.racine.successeurs.extend(successeurs)
                    
    def __repr__(self) -> str:
        return self.noeud.__str__()

    def __str__(self) -> str:
        return self.noeud.__str__()