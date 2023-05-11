import pygame

# creer une classe qui vas s'occuper des animations


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"assets/{sprite_name}.png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0  # commencer l'animation à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # definir une methode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    # definir une methode pour animer le sprite

    def animate(self, loop=False):

        # verrifier si l'animation de cette antiter est active
        if self.animation:
            # Passer à l'image suivante
            self.current_image += 1

            # verrifier si on a à atteint la fin de l'animation
            if self.current_image >= len(self.images):  # type: ignore
                # remetre l'animation au depart
                self.current_image = 0

                # Verrifier si l'animation est en mode boucle
                if loop is False:
                    # desactivation de l'animation
                    self.animation = False

            # modifier l'image précedente par la suivante
            self.image = self.images[self.current_image]  # type: ignore
            self.image = pygame.transform.scale(self.image, self.size)


# definire une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # Charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # Reccuperer le chemein du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # Boucler sur chaque image dan ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + ".png"
        image = pygame.image.load(image_path)
        images.append(image)

    # Renvoyer le contenu de la liste d'images
    return images


# definir un dictionnaire qui va contenir les images chargées de chaque sprite
# mummy -> [...mummy1.png, ...mummy2.png, ...]
animations = {
    "mummy": load_animation_images("mummy"),
    "player": load_animation_images("player"),
    "alien": load_animation_images("alien"),
}
