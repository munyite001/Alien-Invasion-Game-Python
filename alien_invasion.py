""""    Creating an empty pygame window and responding to user input    """
import sys

import pygame

from settings import Settings

from ship import Ship

from bullets import Bullet

from aliens import Alien

class AlienInvasion:
    """ Overall class to manage game assets and behavior """
    def __init__(self):
        """ Initialize the game, and create game resources  """
        pygame.init()

        self.settings = Settings()

        """
            screen_width = self.settings.screen_width

            screen_height = self.settings.screen_height

            self.screen = pygame.display.set_mode((screen_width,screen_height))
        """
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height


        pygame.display.set_caption("Alien Invasion")    #  Setting the title of the game in the game window
        
        
        self.ship = Ship(self)  #Creating an instance of the ship class we imported

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.__create_alien_fleet()

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            self._check_events()
            self.ship.update()  
            self._update_bullets() 
            self._update_screen()    



    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    



    

    """ Function to check key down events  """
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
        #   Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_LEFT:
        #   Move the ship to the left
            self.ship.moving_left = True   
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    """ Function to check key up events  """
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False  


    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group """  
        if len(self.bullets) < self.settings.bullets_count:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet positions and get rid of old bullets"""
        #Update bullet positions
        self.bullets.update()

        #delete old bullets

        #Delete old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def __create_alien_fleet(self):
        """Create the fleet of aliens"""
        #Make an alien
        alien = Alien(self)
        self.aliens.add(alien)




    def _update_screen(self):
        #   Update images on the screen, and flip to the new screen
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        pygame.display.flip()




if __name__ == '__main__':
    #   Make a game instance and Run the game.
    ai = AlienInvasion()
    ai.run_game()