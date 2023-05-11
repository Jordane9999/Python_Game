import pygame
import math
from game import Game

# intialiser le module
pygame.init()

# definir une clock (charger)
clock = pygame.time.Clock()
FPS = 60

# La taille fixe de la fenetre
size_x = 1080
size_y = 720

# Generer la fenetre de notre Jeu
# Permet de donné le nom a la fenetre
pygame.display.set_caption("Comet fall Game")
# Permet de mettre en place la fenetre
screen = pygame.display.set_mode((size_x, size_y))

# importer et charger l'arière plant de notre jeu
# Permet de charger l'image as un endroit specifique
background = pygame.image.load("assets/bg.jpg")

# import et charger notre bannière
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)  # type: ignore

# import et charger notre bouton pour lancer la partie
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(
    (screen.get_width() / 3.33) + 10)  # type: ignore
play_button_rect.y = math.ceil(screen.get_height() / 2)  # type: ignore

# charger notre jeu
game = Game()


runing = True

# Boucle tant que cette condiction est vrai
while runing:

    # Appliquer l'arriere plant du jeu
    screen.blit(background, (0, -200))

    # Verrifier si notre jeu a commencer ou non
    if game.is_playing:
        # declencher les instruction de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commencer
    else:
        # ajouter un bouton de demarage a mon ecran
        screen.blit(play_button, play_button_rect)

        # ajouter mon ecran de bienvenue
        screen.blit(banner, banner_rect)

    # Mettre ajour l'ecran
    pygame.display.flip()

    # Verrifier Si le joueur  ferme cette fenetre
    for event in pygame.event.get():
        # Verrifier que l'evenement est la fermeture de la fenetre
        if event.type == pygame.QUIT:
            runing = False
            pygame.quit()
            print("fermeture du jeu")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchée pour lancée notre projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # mettre le jeu en mode lancer
                    game.start()
                    # Jouer le son
                    game.sound_manager.play('click')
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verrifier si la sourie est en collision avec le bouton du joueur
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                game.start()
                # Jouer le son
                game.sound_manager.play('click')
# fixer le nombre de fps sur ma clock
clock.tick(FPS)
