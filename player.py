import pygame
from projectile import Projectile
import animation

# Creer une classe qui va representer le joueur


class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100  # C'est le point de vie du joueur
        self.max_health = 100  # C'est le point de vie maximal du joueur
        self.attack = 10  # C'est le point de vie que coute une attack
        self.velocity = 10  # C'est la vitesse du joueur
        # Creation d'un group de projectiles
        # Maintenant chaque projectile qui sera lancer va etre ranger dans ce groupe
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/player.png")
        # permet de recuperrer le rectangle le quelle se trouve l'image
        self.rect = self.image.get_rect()

        # Repositonnement du joueur sur l'axe X et Y sur l'ecran
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            # Infliger des degats au joueur
            self.health -= amount
        else:
            # si le joueur n'a plus de point de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # definire une couleu pour notre jauge de vie (vert claire)
        bar_color = (111, 210, 46)

        # definir la couleur pour l'arrière plan de la jauge (gris foncé)
        back_bar_color = (60, 63, 60)

        # definir la position de notre jauge de vie ainssi que sa largeur et son epaisseur bar_positon = [x, y, w, h]
        bar_positon = [self.rect.x + 50, self.rect.y + 20, self.health, 7]

        # definir la position de l'arrière plan de notre jauge de vie
        back_bar_positon = [self.rect.x + 50,
                            self.rect.y + 20, self.max_health, 7]

        # dessiner l'arrière plan de notre bar de vie d'abord
        pygame.draw.rect(surface, back_bar_color,
                         back_bar_positon)  # type: ignore

        # dessiner notre bar de vie
        pygame.draw.rect(surface, bar_color, bar_positon)

    def launch_projectile(self):
        # creer une nouvelle instance de la classe projectille
        projectile = Projectile(self)
        # permet de creer un groupe de projectile
        self.all_projectiles.add(projectile)
        # demarrer l'animation du lancer
        self.start_animation()
        # jouer le son
        self.game.sound_manager.play('tir')

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        else:
            pass

    def move_left(self):
        self.rect.x -= self.velocity
