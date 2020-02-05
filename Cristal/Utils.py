import random

class Tableau():
    def __init__(self, largeur, hauteur):
        self.tab = []
        for i in range(0, largeur):
            ligne = []
            for i in range(0, hauteur):
                ligne.append(None)
            tab.append(ligne)

    def getCase(self, x, y):
        if x < len(self.tab) and y < len(self.tab[x]):
            return tab[x][y]
        else:
            print("Impossible de retourner la valeur : Erreur de dimension")

    def setCase(self, x, y, value):
        if x < len(self.tab) and y < len(self.tab[x]):
            tab[x][y] = value
        else:
            print("Impossible de set la valeur : Erreur de dimension")

def randomColor():
    return (random.choice(range(256)), random.choice(range(256)), random.choice(range(256)), 1)