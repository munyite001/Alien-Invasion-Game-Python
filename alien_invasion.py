""""    Creating an empty pygame window and responding to user input    """

import sys

import pygame

from settings import Settings

from ship import Ship

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

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()          

            

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    

    def _update_screen(self):
        #   Update images on the screen, and flip to the new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

    

    """ Function to check key down events  """
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
        #   Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_LEFT:
        #   Move the ship to the left
            self.ship.moving_left = True   

    """ Function to check key up events  """
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False    


if __name__ == '__main__':
    #   Make a game instance and Run the game.
    ai = AlienInvasion()
    ai.run_game()