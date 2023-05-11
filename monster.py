import pygame
import random
import animation

# Creation d'une classe qui vas gerer la notion de monstre sur notre jeu


class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()

        # Repositonnement du joueur sur l'axe X et Y sur l'ecran
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset

        self.loot_amount = 10

        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # Infliger des degats
        self.health -= amount

        # Verrifer si son nouveau nombre de points de vie est infereur ou egale à 0
        if self.health <= 0:
            # supprimer (Reapparaitre comme un nouveaux monstre)
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            # ajouter le nombre de point au score
            self.game.add_score(self.loot_amount)
            self.velocity = random.randint(1, self.default_speed)

            # si la barre est charger as sont maximum
            if self.game.comet_event.is_full_loaded():
                # retirer du jeu les monstres
                self.game.all_monsters.remove(self)

                # Appeler la methode pour essayer de declencher la pluie de comets
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # definire une couleu pour notre jauge de vie (vert claire)
        bar_color = (111, 210, 46)

        # definir la couleur pour l'arrière plan de la jauge (gris foncé)
        back_bar_color = (60, 63, 60)

        # definir la position de notre jauge de vie ainssi que sa largeur et son epaisseur bar_positon = [x, y, w, h]
        bar_positon = [self.rect.x + 10, self.rect.y - 10, self.health, 5]

        # definir la position de l'arrière plan de notre jauge de vie
        back_bar_positon = [self.rect.x + 10,
                            self.rect.y - 10, self.max_health, 5]

        # dessiner l'arrière plan de notre bar de vie d'abord
        pygame.draw.rect(surface, back_bar_color,
                         back_bar_positon)  # type: ignore

        # dessiner notre bar de vie
        pygame.draw.rect(surface, bar_color, bar_positon)

    def forward(self):
        # le deplacement ne se fait que si in n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en colision avec le joueur
        else:
            # Infliger des degats
            self.game.player.damage(self.attack)


# definir une classe pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)


# definir une classe pour l'alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 140)
        self.health = 250
        self.max_health = 250
        self.attack = 0.9
        self.set_speed(1)
        self.set_loot_amount(80)
