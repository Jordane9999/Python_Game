import pygame


# Creeation de la classe qui va gerer le projectile de notre jeu
class Projectile(pygame.sprite.Sprite):
    
    # definir le constructeur de cette classe
    def __init__(self, player) :
        super().__init__()
        self.velocity = 5 # La vitess du projectile
        # Reccuperer les attribut du player
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        # Redimentionner l'image (Reduire)
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect() # Reccupere le positionnement du rectangle de l'image
        
        # Repositonnement du joueur sur l'axe X et Y sur l'ecran
        self.rect.x = player.rect.x + 120 # Donner la position du joueur augmenter d'une valeur pour l'ajuster as la mains du joueur
        self.rect.y = player.rect.y + 80 # Donner la position du joueur augmenter d'une valeur pour l'ajuster as la mains du joueur
        
        # Les attribut pour gerer la rotation
        self.origin_image = self.image # permet de conserver l'image avant de le transformer
        self.angle = 0  
        
        
    # La method qui va permettre de faire tourbilloner le projectile
    def rotate(self) :
          # faire tourner le projectile
          self.angle += 12          
          self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
          self.rect = self.image.get_rect(center=self.rect.center) # a permis de le touner sur son centre
          
          
    # permet de suprimer les element graphique
    def remove(self) :
        self.player.all_projectiles.remove(self)
        
    
        
    # Methode qui gerer le deplacement du projectile
    def move(self):
        self.rect.x += self.velocity
        self.rotate()   
        
        # Verrifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters) :
            # supprimer le projectil
            self.remove()
            
            # Infliger des degat
            monster.damage(self.player.attack)
            
        # Verrifier si notre projectile n'est plus present sur l'ecrant
        if self.rect.x > 1080 :
            # suprimer le projectile (en dehors de l'ecran)
            self.remove()
            print("projectile suprimer")
        
        
        
        