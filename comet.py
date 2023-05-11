import pygame
import random
from monster import Monster, Mummy, Alien

# Créer une classe pour gérer cette comet


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(50, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event  # Reccuperation de donner de comet event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        # Verrifier si le nombre de comet est de 0 as l'ecran
        if len(self.comet_event.all_comets) == 0:
            print("l'evenement est finir")
            # remetre la barre à 0
            self.comet_event.reset_percent()
            # faire apparaitre les 2 premières monstre
            # self.comet_event.game.spawn_monster(Mummy)
            # self.comet_event.game.spawn_monster(Mummy)
            # self.comet_event.game.spawn_monster(Alien)
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # si elle ne tombe pas sur le sol
        if self.rect.y >= 520:
            print("sol")
            # retirer la boule de feu (supprime)
            self.remove()

            # si il n'y as plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                print("l'evenement est finir")
                # remetre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # Verrifier si la boule de feu touche le joueu
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            print("joueur toucher")
            # retirer la boule de feu (supprime)
            self.remove()

            # faire subir un nombre point de degat
            self.comet_event.game.player.damage(20)
