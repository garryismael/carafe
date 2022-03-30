from node import Noeud
from tree import Tree

def chemin(graphe: Tree, but: int):
    path: list[Noeud] = []
    current = graphe
    while current is not None:
        path.append(current.noeud)
        size = len(path)
        if len(current.successeurs) == 0:
            if current.noeud.x == but:
                if path[size-1].x == but:
                    return path
        else:
            path.pop()
            current = current.successeurs.pop(0)
    return path


# @staticmethod
#     def chemin(graphe: Tree, but: int, path: list[Noeud] = []):
#         path.append(graphe.noeud)
#         size = len(path)
#         if len(graphe.successeurs) == 0:
#             if path[size-1].x == but:
#                 return path
#         else:
#             for child in graphe.successeurs:
#                 return Carafe.chemin(child, but, path)
#             path.pop()