import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sound import SoundManager


# Creer une classe qui representer notre jeu
class Game:

    def __init__(self):
        # definir si notre jeu a commencé ou non
        self.is_playing = False
        # Generer le joueur
        # Group de joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # gerer l'evenement
        self.comet_event = CometFallEvent(self)
        # Group de monstre
        self.all_monsters = pygame.sprite.Group()
        # Changer la police de font ajouter
        self.font = pygame.font.Font('assets/my_custom_font.ttf', 25)
        # metre le score à 0
        self.score = 0
        # Toutes les touche qui son actuellment active
        self.pressed = {}
        # gerer lesle son
        self.sound_manager = SoundManager()

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)  # type: ignore
        self.spawn_monster(Mummy)  # type: ignore
        self.spawn_monster(Alien)  # type: ignore

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        # remettre le jeu à neuf, retirer les monstres, remetre le joueur à 100 point de vie, mettre le jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        # jouer le son
        self.sound_manager.play('game_over')

    def update(self, screen):
        # Afficher le score sur l'ecran
        score_text = self.font.render(
            f"Score : {self.score}", 1, (0, 0, 0))  # type: ignore
        screen.blit(score_text, (20, 20))

        # Appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la bar de vie du joueur
        self.player.update_health_bar(screen)

        # Actualiser l'animation du joueur
        self.player.update_animation()

        # Reccuperer les projectile du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Reccuperer les monstre de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # Reccuperer les comets de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # Appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)

        # Appliquer l'enssemble des images de mon groupe de comet
        self.comet_event.all_comets.draw(screen)

        # Actualiser la barre d'evennement du jeu
        self.comet_event.update_bar(screen)

        # Verrifier si le joueur souhaite aller as gauche ou as droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            print("deplacement as droite")
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            print("deplacement as gauche")
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(
            sprite,
            group,
            False,
            pygame.sprite.collide_mask  # type: ignore
        )

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))
