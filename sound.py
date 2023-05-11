import pygame


class SoundManager:

    def __init__(self):
        self.sounds = {
            "click": pygame.mixer.Sound("assets/sounds/click.ogg"),
            "game_over": pygame.mixer.Sound("assets/sounds/game_over.ogg"),
            "tir": pygame.mixer.Sound("assets/sounds/tir.ogg"),
            "meteorite": pygame.mixer.Sound("assets/sounds/meteorite.ogg"),
        }

    def play(self, name):
        self.sounds[name].play()
