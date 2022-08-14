# ALIEN INVASION GAME IN PYTHON DOCUMENTATION
**This is a python project tutorial using pygame**

**Pre-Requisites**
To work on this project, you'll need:
- Basic understanding Python3 syntax
- Solid grasp on Classes in python
- Solid graps of Functions in python
- Installed Pygame
That's it
---
<img src="images/Alien Invasion.png" alt="Alien Invasion Game Screenshot"/>
---
To access the Full project source code and files, visit the repo on [Github](https://github.com/munyite001/Alien-Invasion-Game-Python).
---
##  Pygame
Pygame is a collection of powerful python modules that manage animations, graphics and even sound, to build powerful applications, like games etc
---
###  INSTALLING PYGAME
To install pygame in your computer, open the terminal and run the command
`python3 -m pip install pygame`

Once pygame is installed, you can now start using it in your programs, by importing it.
`import pygame`

**Now we're good to go**

**Project Definition**
***In Alien Invasion, the player controls a rocket ship that appears***
***at the bottom center of the screen. The player can move the ship***
***right and left using the arrow keys and shoot bullets using the***
***spacebar. When the game begins, a fleet of aliens fills the sky***
***and moves across and down the screen. The player shoots and***
***destroys the aliens. If the player shoots all the aliens, a new fleet***
***appears that moves faster than the previous fleet. If any alien hits***
***the player’s ship or reaches the bottom of the screen, the player***
***loses a ship. If the player loses three ships, the game ends.***

##  Starting the Game Project
We’ll begin building the game by creating an empty Pygame window. Later,
we’ll draw the game elements, such as the ship and the aliens, on this win­
dow. We’ll also make our game respond to user input, set the background
color, and load a ship image.

### Creating a Pygame Window and Responding to User Input
We’ll make an empty Pygame window by creating a class to represent the
game

```python
import sys

import pygame

class AlienInvasion:

    """Overall class to manage game assets and behavior."""

    def __init__(self):

        """Initialize the game, and create game resources."""

        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))  # Attribute representing the game window

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):

        """Start the main loop for the game."""

        while True:

            # Watch for keyboard and mouse events.

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                sys.exit()

            # Make the most recently drawn screen visible.

            pygame.display.flip()

if __name__ == '__main__':

    # Make a game instance, and run the game.

    ai = AlienInvasion()

    ai.run_game()
```

First, we import the sys and pygame modules. 
The pygame module con­tains the functionality we need to make a game. The sys module contains tools to exit the game when the player quits.
Alien Invasion starts as a class called AlienInvasion. In the __init__()
method, the pygame.init() function initializes the background settings that
Pygame needs to work properly. Then we call pygame.display.set_mode() to
create a display window, on which we’ll draw all the game’s graphical ele­ments. The argument (1200, 800) is a tuple that defines the dimensions of
the game window, which will be 1200 pixels wide by 800 pixels high. (You
can adjust these values depending on your display size.) We assign this dis­
play window to the attribute self.screen, so it will be available in all methods
in the class.

The object we assigned to self.screen is called a surface. A surface in
Pygame is a part of the screen where a game element can be displayed.
Each element in the game, like an alien or a ship, is its own surface. The
surface returned by display.set_mode() represents the entire game window.
When we activate the game’s animation loop, this surface will be redrawn
on every pass through the loop, so it can be updated with any changes trig­
gered by user input.

The game is controlled by the run_game() method. This method contains
a while loop that runs continually. The while loop contains an event loop
and code that manages screen updates. An event is an action that the user
performs while playing the game, such as pressing a key or moving the
mouse. To make our program respond to events, we write this event loop to
listen for events and perform appropriate tasks depending on the kinds of
events that occur. The for loop at line (76) is an event loop.
To access the events that Pygame detects, we’ll use the pygame.event.get() function. This function returns a list of events that have taken place
since the last time this function was called. Any keyboard or mouse event
will cause this for loop to run. Inside the loop, we’ll write a series of if
statements to detect and respond to specific events. For example, when the
player clicks the game window’s close button, a pygame.QUIT event is detected
and we call sys.exit() to exit the game.

The call to pygame.display.flip() tells Pygame to make the most
recently drawn screen visible. In this case, it simply draws an empty screen
on each pass through the while loop, erasing the old screen so only the new
screen is visible. When we move the game elements around, pygame.display.flip() continually updates the display to show the new positions of game
elements and hides the old ones, creating the illusion of smooth movement.

At the end of the file, we create an instance of the game, and then call
run_game(). We place run_game() in an if block that only runs if the file is
called directly. When you run this alien_invasion.py file, you should see an
empty Pygame window.

### Setting the background Color
Pygame creates a black screen by default. We can set a differ­ent background color. We’ll do this at the end of the __init__() method.
```python
def __init__(self):
    --snip--
    pygame.display.set_caption("Alien Invasion")
    # Set the background color.
    self.bg_color = (230, 230, 230)

def run_game(self):
    --snip--
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        sys.exit()
    # Redraw the screen during each pass through the loop.
    self.screen.fill(self.bg_color)
```
Colors in Pygame are specified as RGB colors: a mix of red, green,
and blue. Each color value can range from 0 to 255. The color value (255,
0, 0) is red, (0, 255, 0) is green, and (0, 0, 255) is blue. You can mix differ­
ent RGB values to create up to 16 million colors. The color value (230, 230,
230) mixes equal amounts of red, blue, and green, which produces a light
gray background color. We assign this color to self.bg_color at line (146).
At line (154), we fill the screen with the background color using the fill()
method, which acts on a surface and takes only one argument: a color.

### Creating a settings class
Each time we introduce new functionality into the game, we’ll typically
create some new settings as well. Instead of adding settings throughout
the code, let’s write a module called settings that contains a class called
Settings to store all these values in one place. This approach allows us to
work with just one settings object any time we need to access an individual
setting. This also makes it easier to modify the game’s appearance and
behavior as our project grows: to modify the game, we’ll simply change
some values in settings.py, which we’ll create next, instead of searching for
different settings throughout the project.

```python
class Settings:

"""A class to store all settings for Alien Invasion."""

    def __init__(self):

        """Initialize the game's settings."""

        # Screen settings

        self.screen_width = 1200

        self.screen_height = 800

        self.bg_color = (230, 230, 230)

```
Then we'll need to make an instance of Settings in the project and use it to access our settings, by modifying alien_invasion.py as follows:

```python
# AlienInvasion.py 
import pygame

from settings import Settings

class AlienInvasion:

    """Overall class to manage game assets and behavior."""

    def __init__(self):

        """Initialize the game, and create game resources."""

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, 
        self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        
        --snip--
        # Redraw the screen during each pass through the loop.

        self.screen.fill(self.settings.bg_color)

        # Make the most recently drawn screen visible.

        pygame.display.flip()
```
We import Settings into the main program file. Then we create an
instance of Settings and assign it to self.settings at line (212), after making the call to pygame.init(). When we create a screen, we use the screen_width and
screen_height attributes of self.settings, and then we use self.settings to
access the background color when filling the screen as well.
When you run alien_invasion.py now you won’t yet see any changes,
because all we’ve done is move the settings we were already using else­
where. Now we’re ready to start adding new elements to the screen.

### Adding the Ship Image
Let’s add the ship to our game. To draw the player’s ship on the screen,
we’ll load an image and then use the Pygame blit() method to draw the
image.

You can find the ship.bmp image file in the ![images](images/alien.bmp) folder

### Creating the Ship class
After choosing an image for the ship, we need to display it on the screen. To
use our ship, we’ll create a new ship module that will contain the class Ship.
This class will manage most of the behavior of the player’s ship:

```python
#ship.py
import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):

        """Initialize the ship and set its starting position."""

        self.screen = ai_game.screen

        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.

        self.image = pygame.image.load('images/ship.bmp')

        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):

        """Draw the ship at its current location."""

        self.screen.blit(self.image, self.rect)

```

Pygame is efficient because it lets you treat all elements like rect­angles (rects), even if they’re not exactly shaped like rectangles. Treating an element as a rectangle is efficient because rectangles are simple geo­metric shapes. When Pygame needs to figure out whether two ele­ments have collided, for example, it can do this more quickly if it treats each object as a rectangle. This approach usually works well enough that no one playing the game will notice that we’re not working with the exact shape of each game element. We’ll treat the ship and the screen as rect­angles in this class.

We import the pygame module before defining the class. The __init__()
method of Ship takes two parameters: the self reference and a reference to
the current instance of the AlienInvasion class. This will give Ship access to
all the game resources defined in AlienInvasion. At line(261) we assign the screen
to an attribute of Ship, so we can access it easily in all the methods in this
class. At line(263) we access the screen’s rect attribute using the get_rect() method and assign it to self.screen_rect. Doing so allows us to place the ship in the correct location on the screen. To load the image, we call pygame.image.load() and give it the loca­tion of our ship image. This function returns a surface representing the ship, which we assign to self.image. When the image is loaded, we call get_rect() to access the ship surface’s rect attribute so we can later use it to place the ship.

When you’re working with a rect object, you can use the x- and y-coordi­nates of the top, bottom, left, and right edges of the rectangle, as well as the
center, to place the object. You can set any of these values to establish the
current position of the rect. When you’re centering a game element, work
with the center, centerx, or centery attributes of a rect. When you’re working
at an edge of the screen, work with the top, bottom, left, or right attributes.
There are also attributes that combine these properties, such as midbottom,
midtop, midleft, and midright. When you’re adjusting the horizontal or verti­
cal placement of the rect, you can just use the x and y attributes, which are
the x- and y-coordinates of its top-left corner.

***Note***
*In Pygame, the origin (0, 0) is at the top-left corner of the screen and* *coordinates increase as you go down and to the right. On a 1200 by 800 screen* *the origin is at the top-left corner, and the bottom-right corner has the* *coordinates (1200, 800).*
***These coordinates refer to the game window, not the physical screen.***

We’ll position the ship at the bottom center of the screen. To do so,
make the value of self.rect.midbottom match the midbottom attribute of the
screen’s rect. Pygame uses these rect attributes to position the ship
image so it’s centered horizontally and aligned with the bottom of the
screen.
At line(275), we define the blitme() method, which draws the image to the
screen at the position specified by self.rect.

####    Drawing the Ship to the Screen
Now let’s update alien_invasion.py so it creates a ship and calls the ship’s
blitme() method:

```python
#Alien_invasion.py
--snip--

from settings import Settings

from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
            
        --snip--

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):

        --snip--

        # Redraw the screen during each pass through the loop.

        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        # Make the most recently drawn screen visible.

        pygame.display.flip()

        --snip--
```

We import Ship and then make an instance of Ship after the screen
has been created. The call to Ship() requires one argument, an instance
of AlienInvasion. The self argument here refers to the current instance of
AlienInvasion. This is the parameter that gives Ship access to the game’s
resources, such as the screen object. We assign this Ship instance to
self.ship.
After filling the background, we draw the ship on the screen by calling
ship.blitme(), so the ship appears on top of the background.
When you run alien_invasion.py now, you should see an empty game
screen with the rocket ship sitting at the bottom center

###    Refactoring Our Code
Refactoring simplifies the structure of the code you’ve already
written, making it easier to build on. In this section, we’ll break the run_game()
method, which is getting lengthy, into two helper methods. A helper method
does work inside a class but isn’t meant to be called through an instance. In
Python, a single leading underscore indicates a helper method.

####    The _check_events() Method
We’ll move the code that manages events to a separate method called
_check_events(). This will simplify run_game() and isolate the event manage­
ment loop. Isolating the event loop allows you to manage events separately
from other aspects of the game, such as updating the screen.
Here’s the AlienInvasion class with the new _check_events() method,
which only affects the code in run_game():

```python
#Alien_invasion.py

def run_game(self):

    """Start the main loop for the game."""

    while True:

        self._check_events()# Redraw the screen during each pass through the loop.

        --snip--

def _check_events(self):

    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

        sys.exit()
```

####    The _update_screen() Method
To further simplify run_game(), we’ll move the code for updating the screen
to a separate method called _update_screen():
```python
#Alien_invasion.py
def run_game(self):

    """Start the main loop for the game."""

    while True:

        self._check_events()

        self._update_screen()

def _check_events(self):

    --snip--

def _update_screen(self):

    """Update images on the screen, and flip to the new screen."""

    self.screen.fill(self.settings.bg_color)

    self.ship.blitme()

    pygame.display.flip()
```

### Piloting The Ship

Next, we’ll give the player the ability to move the ship right and left. We’ll
write code that responds when the player presses the right or left arrow key.
We’ll focus on movement to the right first, and then we’ll apply the same prin­
ciples to control movement to the left. As we add this code, you’ll learn how to
control the movement of images on the screen and respond to user input.

####    Responding to a Keypress
Whenever the player presses a key, that keypress is registered in Pygame as
an event. Each event is picked up by the pygame.event.get() method. We need
to specify in our _check_events() method what kind of events we want the
game to check for. Each keypress is registered as a KEYDOWN event.
When Pygame detects a KEYDOWN event, we need to check whether the
key that was pressed is one that triggers a certain action. For example, if the
player presses the right arrow key, we want to increase the ship’s rect.x value
to move the ship to the right:

~~~python
#Alien_invasion.py

def _check_events(self):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:

            # Move the ship to the right.

            self.ship.rect.x += 1
~~~

Inside _check_events() we add an elif block to the event loop to respond
when Pygame detects a KEYDOWN event. We check whether the key pressed,
event.key, is the right arrow key. The right arrow key is represented by
pygame.K_RIGHT. If the right arrow key was pressed, we move the ship to the
right by increasing the value of self.ship.rect.x by 1.
When you run alien_invasion.py now, the ship should move to the right
one pixel every time you press the right arrow key. That’s a start, but it’s not
an efficient way to control the ship. Let’s improve this control by allowing
continuous movement.

#### Allowing Continuous Movement

When the player holds down the right arrow key, we want the ship to
continue moving right until the player releases the key. We’ll have the
game detect a pygame.KEYUP event so we’ll know when the right arrow key is
released; then we’ll use the KEYDOWN and KEYUP events together with a flag
called moving_right to implement continuous motion.

When the moving_right flag is False, the ship will be motionless. When
the player presses the right arrow key, we’ll set the flag to True, and when the
player releases the key, we’ll set the flag to False again.
The Ship class controls all attributes of the ship, so we’ll give it an attri-
bute called moving_right and an update() method to check the status of the
moving_right flag. The update() method will change the position of the ship if
the flag is set to True. We’ll call this method once on each pass through the
while loop to update the position of the ship.
Here are the changes to Ship:

```python
ship.py
class Ship:
"""A class to manage the ship."""
    def __init__(self, ai_game):

        --snip--

        # Start each new ship at the bottom center of the screen.

        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag

        self.moving_right = False
        
    def update(self):

        """Update the ship's position based on the movement flag."""

        if self.moving_right:

            self.rect.x += 1

    def blitme(self):

        --snip--
```

We add a self.moving_right attribute in the __init__() method and set it
to False initially.
Then we add update(), which moves the ship right if the
flag is True.
The update() method will be called through an instance of
Ship, so it’s not considered a helper method.

Now we need to modify _check_events() so that moving_right is set to True
when the right arrow key is pressed and False when the key is released:
```python
#Alien_invasion.py

def _check_events(self):

    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():

        --snip--

    elif event.type == pygame.KEYDOWN:

        if event.key == pygame.K_RIGHT:

            self.ship.moving_right = True

    elif event.type == pygame.KEYUP:

        if event.key == pygame.K_RIGHT:

            self.ship.moving_right = False

```
we modify how the game responds when the player presses the
right arrow key: instead of changing the ship’s position directly, we merely
set moving_right to True. Then we add a new elif block at line (556), which responds to KEYUP events. When the player releases the right arrow key (K_RIGHT), we set moving_right to False.

Next, we modify the while loop in run_game() so it calls the ship’s update()
method on each pass through the loop:
```python
#Alien_invasion.py
def run_game(self):

    """Start the main loop for the game."""

    while True:

        self._check_events()

        self.ship.update()

        self._update_screen()

```

The ship’s position will be updated after we’ve checked for keyboard
events and before we update the screen. This allows the ship’s position to be
updated in response to player input and ensures the updated position will
be used when drawing the ship to the screen.

When you run alien_invasion.py and hold down the right arrow key, the
ship should move continuously to the right until you release the key.


####    Moving Both Left and Right
Now that the ship can move continuously to the right, adding movement to
the left is straightforward. Again, we’ll modify the Ship class and the _check
_events() method. Here are the relevant changes to __init__() and update()
in Ship:

```python
ship.py
def __init__(self, ai_game):

    --snip--

    # Movement flags

    self.moving_right = False

    self.moving_left = False

def update(self):

    """Update the ship's position based on movement flags."""

    if self.moving_right:

        self.rect.x += 1

    if self.moving_left:

        self.rect.x -= 1
```

In __init__(), we add a self.moving_left flag. In update(), we use two
separate if blocks rather than an elif to allow the ship’s rect.x value to be
increased and then decreased when both arrow keys are held down. This
results in the ship standing still. If we used elif for motion to the left, the right arrow key would always have priority. Doing it this way makes the
movements more accurate when switching from right to left when the player
might momentarily hold down both keys.

We have to make two adjustments to _check_events():
```python
#Alien_invasion.py

def _check_events(self):

    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():

        --snip--

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:

                self.ship.moving_right = True

            elif event.key == pygame.K_LEFT:

                self.ship.moving_left = True

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_RIGHT:

                self.ship.moving_right = False

            elif event.key == pygame.K_LEFT:

                self.ship.moving_left = False

```

If a KEYDOWN event occurs for the K_LEFT key, we set moving_left to True. If a
KEYUP event occurs for the K_LEFT key, we set moving_left to False. We can use
elif blocks here because each event is connected to only one key. If the player
presses both keys at once, two separate events will be detected.

When you run alien_invasion.py now, you should be able to move the ship
continuously to the right and left. If you hold down both keys, the ship should
stop moving.

Next, we’ll further refine the ship’s movement. Let’s adjust the ship’s
speed and limit how far the ship can move so it can’t disappear off the sides
of the screen.

####    Adjusting the Ship’s Speed
Currently, the ship moves one pixel per cycle through the while loop, but we
can take finer control of the ship’s speed by adding a ship_speed attribute to
the Settings class. We’ll use this attribute to determine how far to move the
ship on each pass through the loop.

```python
#Settings.py
class Settings:

    """A class to store all settings for Alien Invasion."""

    def __init__(self):

        --snip--

        # Ship settings
        
        self.ship_speed = 1.5
```
We set the initial value of ship_speed to 1.5. When the ship moves
now, its position is adjusted by 1.5 pixels rather than 1 pixel on each pass
through the loop.

However, rect attributes such as x store only integer values, so we need to
make some modifications to Ship:
```python
#ship.py

class Ship:

    """A class to manage the ship."""
    
    def __init__(self, ai_game):

        """Initialize the ship and set its starting position."""
        
        self.screen = ai_game.screen

        self.settings = ai_game.settings

        --snip--

        # Start each new ship at the bottom center of the screen.

        --snip--

        # Store a decimal value for the ship's horizontal position.

        self.x = float(self.rect.x)

        # Movement flags

        self.moving_right = False

        self.moving_left = False

    def update(self):

        """Update the ship's position based on movement flags."""

        # Update the ship's x value, not the rect.

        if self.moving_right:
            
            self.x += self.settings.ship_speed

        if self.moving_left:

            self.x -= self.settings.ship_speed

        # Update rect object from self.x.

        self.rect.x = self.x

    def blitme(self):

    --snip--
```
We create a settings attribute for Ship, so we can use it in update().
Because we’re adjusting the position of the ship by fractions of a pixel, we
need to assign the position to a variable that can store a decimal value. You
can use a decimal value to set an attribute of rect, but the rect will only
keep the integer portion of that value. To keep track of the ship’s position
accurately, we define a new self.x attribute that can hold decimal values .
We use the float() function to convert the value of self.rect.x to a decimal
and assign this value to self.x.
Now when we change the ship’s position in update(), the value of self.x
is adjusted by the amount stored in settings.ship_speed. After self.x has
been updated, we use the new value to update self.rect.x, which controls
the position of the ship. Only the integer portion of self.x will be stored
in self.rect.x, but that’s fine for displaying the ship.

Now we can change the value of ship_speed, and any value greater than
one will make the ship move faster. This will help make the ship respond
quickly enough to shoot down aliens, and it will let us change the tempo of
the game as the player progresses in gameplay.

####    Limiting the Ship’s Range
At this point, the ship will disappear off either edge of the screen if you
hold down an arrow key long enough. Let’s correct this so the ship stops
moving when it reaches the screen’s edge. We do this by modifying the
update() method in Ship:

```python
#ship.py
def update(self):
    """Update the ship's position based on movement flags."""

    # Update the ship's x value, not the rect.

    if self.moving_right and self.rect.right < self.screen_rect.right:

        self.x += self.settings.ship_speed

    if self.moving_left and self.rect.left > 0:

        self.x -= self.settings.ship_speed

    # Update rect object from self.x.

    self.rect.x = self.x
```

This code checks the position of the ship before changing the value of
self.x. The code self.rect.right returns the x-coordinate of the right edge
of the ship’s rect. If this value is less than the value returned by self.screen
_rect.right, the ship hasn’t reached the right edge of the screen. The same
goes for the left edge: if the value of the left side of the rect is greater than
zero, the ship hasn’t reached the left edge of the screen.

This ensures the ship is within these bounds before adjusting the value of self.x.
When you run alien_invasion.py now, the ship should stop moving at
either edge of the screen. This is pretty cool; all we’ve done is add a condi­tional test in an if statement, but it feels like the ship hits a wall or a force field at either edge of the screen!

####    Refactoring _check_events()
The _check_events() method will increase in length as we continue to develop
the game, so let’s break _check_events() into two more methods: one that
handles KEYDOWN events and another that handles KEYUP events:
```python
#Alien_invasion.py

def _check_events(self):

    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()

        elif event.type == pygame.KEYDOWN:

            self._check_keydown_events(event)

        elif event.type == pygame.KEYUP:

            self._check_keyup_events(event)

def _check_keydown_events(self, event):

        """Respond to keypresses."""

        if event.key == pygame.K_RIGHT:

            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:

            self.ship.moving_left = True

def _check_keyup_events(self, event):

    """Respond to key releases."""

    if event.key == pygame.K_RIGHT:

        self.ship.moving_right = False

    elif event.key == pygame.K_LEFT:

        self.ship.moving_left = False
```
We make two new helper methods: _check_keydown_events() and _check
_keyup_events(). Each needs a self parameter and an event parameter. The
bodies of these two methods are copied from _check_events(), and we’ve
replaced the old code with calls to the new methods. The _check_events()
method is simpler now with this cleaner code structure, which will make it
easier to develop further responses to player input

####    Pressing Q to Quit
Now that we’re responding to keypresses efficiently, we can add another
way to quit the game. It gets tedious to click the X at the top of the game
window to end the game every time you test a new feature, so we’ll add a
keyboard shortcut to end the game when the player presses Q:
```python
#Alien_invasion.py

def _check_keydown_events(self, event):

    --snip--

    elif event.key == pygame.K_LEFT:

        self.ship.moving_left = True

    elif event.key == pygame.K_q:

        sys.exit()
```
In _check_keydown_events(), we add a new block that ends the game when
the player presses Q. Now, when testing, you can press Q to close the game
rather than using your cursor to close the window.

####    Running the Game in Fullscreen Mode
Pygame has a fullscreen mode that you might like better than running the
game in a regular window. Some games look better in fullscreen mode, and
macOS users might see better performance in fullscreen mode.
To run the game in fullscreen mode, make the following changes in
__init__():
```python

#Alien_invasion.py

def __init__(self):

    """Initialize the game, and create game resources."""
    
    pygame.init()

    self.settings = Settings()
    
    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    self.settings.screen_width = self.screen.get_rect().width

    self.settings.screen_height = self.screen.get_rect().height

    pygame.display.set_caption("Alien Invasion")
```
When creating the screen surface, we pass a size of (0, 0) and the
parameter pygame.FULLSCREEN. This tells Pygame to figure out a window size
that will fill the screen. Because we don’t know the width and height of the
screen ahead of time, we update these settings after the screen is created.
We use the width and height attributes of the screen’s rect to update the
s­ettings object.

### Shooting Bullets
At the end of the __init__() method, we’ll update settings.py to include the
values we’ll need for a new Bullet class:
```python
#settings.py
def __init__(self):
    --snip--
    # Bullet settings
    self.bullet_speed = 1.0
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (60, 60, 60)
```
These settings create dark gray bullets with a width of 3 pixels and a
height of 15 pixels. The bullets will travel slightly slower than the ship.

#### Creating the bullet class
Now we will create a bullet.py file to store our Bullet class. 

```python
#bullet.py

import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):

    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
    """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
        self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
```
The Bullet class inherits from Sprite, which we import from the pygame
.sprite module. When you use sprites, you can group related elements in
your game and act on all the grouped elements at once. 
To create a bulletinstance, __init__() needs the current instance of AlienInvasion, and we call super() to inherit properly from Sprite. We also set attributes for the screen and settings objects, and for the bullet’s color.
Then, we create the bullet’s rect attribute. The bullet isn’t based on an
image, so we have to build a rect from scratch using the pygame.Rect() class.
This class requires the x- and y-coordinates of the top-left corner of the 
rect, and the width and height of the rect. We initialize the rect at (0, 0),
but we’ll move it to the correct location in the next line, because the bullet’s
position depends on the ship’s position. We get the width and height of the
bullet from the values stored in self.settings.
Then, we set the bullet’s midtop attribute to match the ship’s midtop attri­
bute. This will make the bullet emerge from the top of the ship, making it
look like the bullet is fired from the ship. We store a decimal value for the
bullet’s y-coordinate so we can make fine adjustments to the bullet’s speed.
Here’s the second part of bullet.py, update() and draw_bullet():

```python
#bullet.py
def update(self):
    """Move the bullet up the screen."""
    # Update the decimal position of the bullet.
    self.y -= self.settings.bullet_speed
    # Update the rect position.
    self.rect.y = self.y

def draw_bullet(self):
    """Draw the bullet to the screen."""
    pygame.draw.rect(self.screen, self.color, self.rect)
```
The update() method manages the bullet’s position. When a bullet is
fired, it moves up the screen, which corresponds to a decreasing y-coordinate
value. To update the position, we subtract the amount stored in settings
.bullet_speed from self.y. We then use the value of self.y to set the value
of self.rect.y.

The bullet_speed setting allows us to increase the speed of the bullets
as the game progresses or as needed to refine the game’s behavior. Once a
bullet is fired, we never change the value of its x-coordinate, so it will travel
vertically in a straight line even if the ship moves.

When we want to draw a bullet, we call draw_bullet(). The draw.rect()
function fills the part of the screen defined by the bullet’s rect with the
color stored in self.color

####    Storing bullets in a group
Now that we have a Bullet class and the necessary settings defined, we can
write code to fire a bullet each time the player presses the spacebar. We’ll
create a group in AlienInvasion to store all the live bullets so we can man­
age the bullets that have already been fired. This group will be an instance
of the pygame.sprite.Group class, which behaves like a list with some extra
functionality that’s helpful when building games. We’ll use this group
to draw bullets to the screen on each pass through the main loop and to
update each bullet’s position.
We’ll create the group in __init__():

```python
#alien_invasion.py

def __init__(self):
    --snip--
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
```
Then we need to update the position of the bullets on each pass
through the while loop:
```python
alien_invasion.py
u
def run_game(self):
    """Start the main loop for the game."""
    while True:
        self._check_events()
        self.ship.update()
        self.bullets.update()
        self._update_screen()
```
When we call update() on a group, the group automatically calls
update() for each sprite in the group. The line self.bullets.update() calls
­bullet.update() for each bullet we place in the group bullets.

#### Firing Bullets
In AlienInvasion, we need to modify _check_keydown_events() to fire a bullet
when the player presses the spacebar. We don’t need to change _check_keyup
_events() because nothing happens when the spacebar is released. We also
need to modify _update_screen() to make sure each bullet is drawn to the
screen before we call flip().

let’s write a new method, _fire_bullet(), to handle the whole process of firing bullets:
```python
#   alien_invasion.py
--snip--

from ship import Ship
from bullet import Bullet

class AlienInvasion:
    --snip--

    def _check_keydown_events(self, event):
        --snip--
        elif event.key == pygame.K_q:
            sys.exit()
        
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        --snip--
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            --snip--
```
First, we import the Bullet class. Then we call _fire_bullet() when the space­
bar is pressed. In _fire_bullet(), we make an instance of Bullet and call it
new_bullet. We then add it to the group bullets using the add() method.
The add() method is similar to append(), but it’s a method that’s written spe­
cifically for Pygame groups.

The bullets.sprites() method returns a list of all sprites in the group
bullets. To draw all fired bullets to the screen, we loop through the sprites
in bullets and call draw_bullet() on each one.
When you run alien_invasion.py now, you should be able to move the ship
right and left, and fire as many bullets as you want. The bullets travel up the
screen and disappear when they reach the top. You
can alter the size, color, and speed of the bullets in settings.py.

#### Deleting Old Bullets
At the moment, the bullets disappear when they reach the top, but only
because Pygame can’t draw them above the top of the screen. The bullets
actually continue to exist; their y-coordinate values just grow increasingly
negative. This is a problem, because they continue to consume memory and
processing power. We need to get rid of these old bullets, or the game will slow down from doing so much unnecessary work. To do this, we need to detect when the
bottom value of a bullet’s rect has a value of 0, which indicates the bullet has
passed off the top of the screen:

```python
alien_invasion.py
def run_game(self):
    """Start the main loop for the game."""
    while True:
        self._check_events()
        self.ship.update()
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                print(len(self.bullets))
                self._update_screen()
```
When you use a for loop with a list (or a group in Pygame), Python
expects that the list will stay the same length as long as the loop is run­
ning. Because we can’t remove items from a list or group within a for loop,
we have to loop over a copy of the group. We use the copy() method to set
up the for loop, which enables us to modify bullets inside the loop. We
check each bullet to see whether it has disappeared off the top of the screen. If it has, we remove it from bullets. We then insert a print() call to
show how many bullets currently exist in the game and verify that they’re
being deleted when they reach the top of the screen.

If this code works correctly, we can watch the terminal output while fir­
ing bullets and see that the number of bullets decreases to zero after each
series of bullets has cleared the top of the screen. After you run the game
and verify that bullets are being deleted properly, remove the print() call. If
you leave it in, the game will slow down significantly because it takes more
time to write output to the terminal than it does to draw graphics to the
game window.

#### Limiting the number of bullets fired at a time
We'll limit the number of bullets fired by the player at any given time in order to make the game a bit more challenging

First, store the number of bullets allowed in settings.py:
```python
#settings.py

    # Bullet settings
    --snip--
    self.bullet_color = (60, 60, 60)
    self.bullets_allowed = 3
```
This limits the player to three bullets at a time. We’ll use this setting in
AlienInvasion to check how many bullets exist before creating a new bullet
in _fire_bullet():

```python

#alien_invasion.py

def _fire_bullet(self):
    """Create a new bullet and add it to the bullets group."""
    if len(self.bullets) < self.settings.bullets_allowed:
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
```
When the player presses the spacebar, we check the length of bullets.
If len(self.bullets) is less than three, we create a new bullet. But if three
bullets are already active, nothing happens when the spacebar is pressed.
When you run the game now, you should be able to fire bullets only in
groups of three.

#### Creating the _update_bullets() Method
We want to keep the AlienInvasion class reasonably well organized, so now
that we’ve written and checked the bullet management code, we can move
it to a separate method. We’ll create a new method called _update_bullets()
and add it just before _update_screen():
```python
alien_invasion.py
def _update_bullets(self):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    self.bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
        if bullet.rect.bottom <= 0:
            self.bullets.remove(bullet)
```
The code for _update_bullets() is cut and pasted from run_game(); all
we’ve done here is clarify the comments.
The while loop in run_game() looks simple again:
```python
#alien_invasion.py
while True:
    self._check_events()
    self.ship.update()
    self._update_bullets()
    self._update_screen()
```
Now our main loop contains only minimal code, so we can quickly read
the method names and understand what’s happening in the game. The
main loop checks for player input, and then updates the position of the
ship and any bullets that have been fired. We then use the updated posi-
tions to draw a new screen.
Run alien_invasion.py one more time, and make sure you can still fire
bullets without errors.

### ALIENS
Placing one alien on the screen will be like placing a ship on the screen. Each
alien’s behavior is controlled by a class called Alien, which we’ll structure
like the Ship class. Choose the image you'll be using in your project and store it in your images folder.

####    Creating the aliens class
Now we’ll write the Alien class and save it as alien.py:
```python
#Aliens.py

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""

        super().__init__()

        self.screen = ai_game.screen
        
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
```
Most of this class is like the Ship class except for the aliens’ placement
on the screen. We initially place each alien near the top-left corner of
the screen; we add a space to the left of it that’s equal to the alien’s width
and a space above it equal to its height so it’s easy to see. We’re mainly
concerned with the aliens’ horizontal speed, so we’ll track the horizontal
position of each alien precisely.

This Alien class doesn’t need a method for drawing it to the screen;
instead, we’ll use a Pygame group method that automatically draws all the
elements of a group to the screen.

#### Creating an instance of an alien
We want to create an instance of Alien so we can see the first alien on
the screen. Because it’s part of our setup work, we’ll add the code for this
instance at the end of the __init__() method in AlienInvasion. Eventually,
we’ll create an entire fleet of aliens, which will be quite a bit of work,
so we’ll make a new helper method called _create_fleet().
I’ll place _create_fleet() just before the
_update_screen() method, but anywhere in AlienInvasion will work. First, we’ll
import the Alien class.
Here are the updated import statements for alien_invasion.py:
```python

#alien_invasion.py

--snip--
from bullet import Bullet
from alien import Alien

```
The updated __init__ method:
```python
#   alien_invasion.py
def __init__(self):
    --snip--
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.aliens = pygame.sprite.Group()
    self._create_fleet()
```
We create a group to hold the fleet of aliens, and we call _create_fleet(),
which follows below.
```python
#   alien_invasion.py
def _create_fleet(self):
    """Create the fleet of aliens."""
    # Make an alien.
    alien = Alien(self)
    self.aliens.add(alien)
```
In this method, we’re creating one instance of Alien, and then adding it
to the group that will hold the fleet. The alien will be placed in the default
upper-left area of the screen, which is perfect for the first alien.

To make the alien appear, we need to call the group’s draw() method in
_update_screen():

```python
#   alien_invasion.py
def _update_screen(self):
    --snip--
    for bullet in self.bullets.sprites():
        bullet.draw_bullet()

    self.aliens.draw(self.screen)

    pygame.display.flip()

```
When you call draw() on a group, Pygame draws each element in the
group at the position defined by its rect attribute. The draw() method
requires one argument: a surface on which to draw the elements from the
group.
When you run the game now in alien_invasion.py, you shoud see the first alien displayed on the screen

####    Building the Alien fleet
To draw a fleet, we need to figure out how many aliens can fit across the
screen and how many rows of aliens can fit down the screen. We’ll first fig-
ure out the horizontal spacing between aliens and create a row; then we’ll
determine the vertical spacing and create an entire fleet.

####    Determining How Many Aliens Fit in a Row
To figure out how many aliens fit in a row, let’s look at how much horizontal
space we have. The screen width is stored in settings.screen_width, but we
need an empty margin on either side of the screen. We’ll make this margin
the width of one alien. Because we have two margins, the available space for
aliens is the screen width minus two alien widths:

`available_space_x = settings.screen_width – (2 * alien_width)`

We also need to set the spacing between aliens; we’ll make it one alien
width. The space needed to display one alien is twice its width: one width
for the alien and one width for the empty space to its right. To find the
number of aliens that fit across the screen, we divide the available space by
two times the width of an alien. We use floor division (//), which divides two
numbers and drops any remainder, so we’ll get an integer number of aliens:

`number_aliens_x = available_space_x // (2 * alien_width)`

####    Creating a Row of Aliens
We’re ready to generate a full row of aliens. Because our code for making
a single alien works, we’ll rewrite _create_fleet() to make a whole row of
aliens:
```python
#alien_invasion.py

def _create_fleet(self):
    """Create the fleet of aliens."""

    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(self)
    alien_width = alien.rect.width
    available_space_x = self.settings.screen_width - (2 * alien_width)
    number_aliens_x = available_space_x // (2 * alien_width)

    # Create the first row of aliens.
    for alien_number in range(number_aliens_x):

        # Create an alien and place it in the row.
        alien = Alien(self)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)
```
We’ve already thought through most of this code. We need to know the
alien’s width and height to place aliens, so we create an alien before
we perform calculations. This alien won’t be part of the fleet, so don’t add
it to the group aliens. Then we get the alien’s width from its rect attribute
and store this value in alien_width so we don’t have to keep working through
the rect attribute. Then we calculate the horizontal space available for aliens
and the number of aliens that can fit into that space.
Next, we set up a loop that counts from 0 to the number of aliens we
need to make. In the main body of the loop, we create a new alien and
then set its x-coordinate value to place it in the row. Each alien is pushed
to the right one alien width from the left margin. Next, we multiply the
alien width by 2 to account for the space each alien takes up, including the
empty space to its right, and we multiply this amount by the alien’s position
in the row. We use the alien’s x attribute to set the position of its rect. Then
we add each new alien to the group aliens.

When you run Alien Invasion now, you should see the first row of aliens.
The first row is offset to the left, which is actually good for gameplay.
The reason is that we want the fleet to move right until it hits the edge
of the screen, then drop down a bit, then move left, and so forth. Like the
classic game Space Invaders, this movement is more interesting than having
the fleet drop straight down. We’ll continue this motion until all aliens are
shot down or until an alien hits the ship or the bottom of the screen.

####    Refactoring _create_fleet()
If the code we’ve written so far was all we need to create a fleet, we’d prob-
ably leave _create_fleet() as is. But we have more work to do, so let’s clean
up the method a bit. We’ll add a new helper method, _create_alien(), and
call it from _create_fleet():
```python
#alien_invasion.py

def _create_fleet(self):
    --snip--

    # Create the first row of aliens.
    for alien_number in range(number_aliens_x):
        self._create_alien(alien_number)

def _create_alien(self, alien_number):
    """Create an alien and place it in the row."""

    alien = Alien(self)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    self.aliens.add(alien)

```
The method _create_alien() requires one parameter in addition to self:
it needs the alien number that’s currently being created. We use the same
body we made for _create_fleet() except that we get the width of an alien
inside the method instead of passing it as an argument. This refactoring
will make it easier to add new rows and create an entire fleet.

####    Adding Rows
To finish the fleet, we’ll determine the number of rows that fit on the screen
and then repeat the loop for creating the aliens in one row until we have
the correct number of rows. To determine the number of rows, we find the
available vertical space by subtracting the alien height from the top, the ship
height from the bottom, and two alien heights from the bottom of the screen:

`available_space_y = settings.screen_height – (3 * alien_height) – ship_height`

The result will create some empty space above the ship, so the player
has some time to start shooting aliens at the beginning of each level.
Each row needs some empty space below it, which we’ll make equal to the
height of one alien. To find the number of rows, we divide the available space
by two times the height of an alien. We use floor division because we can only
make an integer number of rows.

`number_rows = available_height_y // (2 * alien_height)`

Now that we know how many rows fit in a fleet, we can repeat the code
for creating a row:
```python
#alien_invasion.py

def _create_fleet(self):
    --snip--
    alien = Alien(self)
    alien_width, alien_height = alien.rect.size
    available_space_x = self.settings.screen_width - (2 * alien_width)
    number_aliens_x = available_space_x // (2 * alien_width)
    
    # Determine the number of rows of aliens that fit on the screen.
    ship_height = self.ship.rect.height
    available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)

    number_rows = available_space_y // (2 * alien_height)

    # Create the full fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number, row_number)

def _create_alien(self, alien_number, row_number):
    """Create an alien and place it in the row."""

    alien = Alien(self)
    alien_width, alien_height = alien.rect.size
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    self.aliens.add(alien)
```
We need the width and height of an alien, so at we use the attribute
size, which contains a tuple with the width and height of a rect object. To
calculate the number of rows we can fit on the screen, we write our available
_space_y calculation right after the calculation for available_space_x. The
calculation is wrapped in parentheses so the outcome can be split over two
lines, which results in lines of 79 characters or less.

To create multiple rows, we use two nested loops: one outer and one
inner loop. The inner loop creates the aliens in one row. The outer loop
counts from 0 to the number of rows we want; Python uses the code for
making a single row and repeats it number_rows times.

To nest the loops, write the new for loop and indent the code you want
to repeat.  Now when we call _create_alien(), we
include an argument for the row number so each row can be placed farther
down the screen.
The definition of _create_alien() needs a parameter to hold the row
number. Within _create_alien(), we change an alien’s y-coordinate value
when it’s not in the first row by starting with one alien’s height to c­reate
empty space at the top of the screen. Each row starts two alien heights below
the previous row, so we multiply the alien height by two and then by the row
number. The first row number is 0, so the vertical placement of the first row
is unchanged. All subsequent rows are placed further down the screen.
When you run the game now, you should see a full fleet of aliens.


####    Making the Fleet Move
Now let’s make the fleet of aliens move to the right across the screen until
it hits the edge, and then make it drop a set amount and move in the other
direction. We’ll continue this movement until either all aliens have been shot down or
one collides with the ship, or one reaches the bottom of the screen. Let’s
begin by making the fleet move to the right.

####    Moving the Aliens Right
To move the aliens, we’ll use an update() method in alien.py, which we’ll
call for each alien in the group of aliens. First, add a setting to control the
speed of each alien:

```python
#settings.py

def __init__(self):
    --snip--
    # Alien settings
    self.alien_speed = 1.0
```
Then use this setting to implement update():

```python
#alien.py

def __init__(self, ai_game):
    """Initialize the alien and set its starting position."""

    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    --snip--
    
def update(self):
    """Move the alien to the right."""
    
    self.x += self.settings.alien_speed
    self.rect.x = self.x

```
We create a settings parameter in __init__() so we can access the alien’s
speed in update(). Each time we update an alien’s position, we move it to the
right by the amount stored in alien_speed. We track the alien’s exact position
with the self.x attribute, which can hold decimal values. We then use the
value of self.x to update the position of the alien’s rect.
In the main while loop, we already have calls to update the ship and
bullet positions. Now we’ll add a call to update the position of each alien
as well:
```python
#alien_invasion.py

while True:
    self._check_events()
    self.ship.update()
    self._update_bullets()
    self._update_aliens()
    self._update_screen()

```
We’re about to write some code to manage the movement of the fleet,
so we create a new method called _update_aliens(). We set the aliens’ posi-
tions to update after the bullets have been updated, because we’ll soon be
checking to see whether any bullets hit any aliens.
Where you place this method in the module is not critical. But to
keep the code organized, we’ll place it just after _update_bullets() to match
the order of method calls in the while loop. Here’s the first version of
_update_aliens():
```python
#alien_invasion.py

def _update_aliens(self):
    """Update the positions of all aliens in the fleet."""

    self.aliens.update()
```
We use the update() method on the aliens group, which calls each
alien’s update() method. When you run Alien Invasion now, you should see
the fleet move right and disappear off the side of the screen.

####    Creating Settings for Fleet Direction
Now we’ll create the settings that will make the fleet move down the screen
and to the left when it hits the right edge of the screen. Here’s how to imple-
ment this behavior:

```python
#settings.py

# Alien settings
self.alien_speed = 1.0
self.fleet_drop_speed = 10

# fleet_direction of 1 represents right; -1 represents left.
self.fleet_direction = 1
```
The setting fleet_drop_speed controls how quickly the fleet drops down
the screen each time an alien reaches either edge. It’s helpful to separate
this speed from the aliens’ horizontal speed so you can adjust the two
speeds independently.
To implement the setting fleet_direction, we could use a text value, such
as 'left' or 'right', but we’d end up with if-elif statements testing for the
fleet direction. Instead, because we have only two directions to deal with,
let’s use the values 1 and −1, and switch between them each time the fleet
changes direction. (Using numbers also makes sense because moving right
involves adding to each alien’s x-coordinate value, and moving left involves
subtracting from each alien’s x-coordinate value.)

####    Checking Whether an Alien Has Hit the Edge
We need a method to check whether an alien is at either edge, and we need
to modify update() to allow each alien to move in the appropriate direction.
This code is part of the Alien class:

```python
#alien.py

def check_edges(self):
    """Return True if alien is at edge of screen."""

    screen_rect = self.screen.get_rect()
    if self.rect.right >= screen_rect.right or self.rect.left <= 0:
        return True

def update(self):
    """Move the alien right or left."""

    self.x += (self.settings.alien_speed *
    self.settings.fleet_direction)
    self.rect.x = self.x
```
We can call the new method check_edges() on any alien to see whether
it’s at the left or right edge. The alien is at the right edge if the right attribute of its rect is greater than or equal to the right attribute of the screen’srect. 
It’s at the left edge if its left value is less than or equal to 0 .
We modify the method update() to allow motion to the left or right
by multiplying the alien’s speed by the value of fleet_direction. If fleet
_direction is 1, the value of alien_speed will be added to the alien’s current
position, moving the alien to the right; if fleet_direction is −1, the value
will be subtracted from the alien’s position, moving the alien to the left.

####    Dropping the Fleet and Changing Direction
When an alien reaches the edge, the entire fleet needs to drop down and
change direction. Therefore, we need to add some code to AlienInvasion
because that’s where we’ll check whether any aliens are at the left or right
edge. We’ll make this happen by writing the methods _check_fleet_edges()
and _change_fleet_direction(), and then modifying _update_aliens().

```python
#alien_invasion.py

def _check_fleet_edges(self):
    """Respond appropriately if any aliens have reached an edge."""

    for alien in self.aliens.sprites():
        if alien.check_edges():
            self._change_fleet_direction()
            break

def _change_fleet_direction(self):
    """Drop the entire fleet and change the fleet's direction."""

    for alien in self.aliens.sprites():
        alien.rect.y += self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1
```
In _check_fleet_edges(), we loop through the fleet and call check_edges()
on each alien. If check_edges() returns True, we know an alien is at an
edge and the whole fleet needs to change direction; so we call _change_fleet
_direction() and break out of the loop v. In _change_fleet_direction(), we
loop through all the aliens and drop each one using the setting fleet_drop
_speed; then we change the value of fleet_direction by multiplying its cur-
rent value by −1. The line that changes the fleet’s direction isn’t part of the
for loop. We want to change each alien’s vertical position, but we only want
to change the direction of the fleet once.

changes to _update_aliens():
```python
#alien_invasion.py

def _update_aliens(self):
    """
    Check if the fleet is at an edge,
    then update the positions of all aliens in the fleet.
    """
    self._check_fleet_edges()
    self.aliens.update()
```
We’ve modified the method by calling _check_fleet_edges() before
updating each alien’s position.
When you run the game now, the fleet should move back and forth
between the edges of the screen and drop down every time it hits an edge.
Now we can start shooting down aliens and watch for any aliens that hit the
ship or reach the bottom of the screen.

####    Shooting Aliens


