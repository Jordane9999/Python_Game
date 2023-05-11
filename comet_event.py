import pygame
from comet import Comet

# Creer une classe pour gérer cette evenement


class CometFallEvent:

    # lors du conten chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False
        # definir un group de sprite pour stocker nos cometes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # boucle pour les valeurs entre 1 et 10
        for i in range(1, 10):
            # faire apparaitre une première boule de feu
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # La jauge d'evenement est totalement chargé
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Pluie de cometes ")
            self.meteor_fall()
            # self.reset_percent()
            self.fall_mode = True  # activer l'evenement

    def update_bar(self, surface):

        # ajouter du pourcentage
        self.add_percent()

        # Appelle de la methode pour essayer de declencher la pluie de comet
        # self.attempt_fall()

        # barre noir en arrière plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # l'axe des abcise ou X
            surface.get_height() - 20,  # l'axe des ordonner ou Y
            surface.get_width(),  # la longueur de la fenetre
            10  # epaisseur de la barre
        ])

        # barre rouge (jauge d'evenement)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l'axe des abcise ou X
            surface.get_height() - 20,  # l'axe des ordonner ou Y
            (surface.get_width() / 100) * \
            self.percent,  # la longueur de la fenetre
            10  # epaisseur de la barre
        ])
