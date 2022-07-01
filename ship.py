import pygame

class Ship:
    """A class to manage the player's ship"""

    def __init__(self,ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load the ship's image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Movement flag
        self.moving_right = False
        self.moving_left = False

        

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        # The code below, cheks that the co-ordinates of the ship's edges are less than the co-ordinates of the screen's edges
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x



    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

