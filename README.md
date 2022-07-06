# ALIEN INVASION GAME IN PYTHON

<img src="images/Alien Invasion.png" alt="Alien invasion Screenshot">

**Pre-Requisites**
To work on this project, you'll need:
- Basic understanding Python3 syntax
- Solid grasp on Classes in python
- Solid graps of Functions in python
- Installed Pygame
That's it
---
##  Project Files

### alien_invasion.py
The main file, alien_invasion.py, contains the AlienInvasion class. This class
creates a number of important attributes used throughout the game: the
settings are assigned to settings, the main display surface is assigned to
screen, and a ship instance is created in this file as well. The main loop of
the game, a while loop, is also stored in this module. The while loop calls
_check_events(), ship.update(), and _update_screen().
The _check_events() method detects relevant events, such as key
presses and releases, and processes each of these types of events through
the methods _check_keydown_events() and _check_keyup_events(). The AlienInvasion class also
contains _update_screen(), which redraws the screen on each pass through
the main loop.
The alien_invasion.py file is the only file you need to run when you want
to play Alien Invasion. The other files—settings.py and ship.py—contain code
that is imported into this file.

### settings.py
The settings.py file contains the Settings class. This class only has an __init__()
method, which initializes attributes controlling the game’s appearance and
the ship’s speed.

### ship.py
The ship.py file contains the Ship class. The Ship class has an __init__()
method, an update() method to manage the ship’s position, and a blitme()
method to draw the ship to the screen. The image of the ship is stored in
ship.bmp, which is in the images folder.


##  Project Resources
To access the Full project source code and files, visit the repo on [Github](https://github.com/munyite001/Alien-Invasion-Game-Python).

### Documentation
To access the full project documentation and step by step tutorial: [Documentation](DOCUMENTATION.md)

### Author
The author of this project is [Emmanuel_Munyite](https://github.com/munyite001)
- Email on <emunyite@gmail.com>
- Linkedin [Emmanuel Munyite](https://www.linkedin.com/in/emmanuel-munyite-68545023a/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3B08aMskKBRQu1mVw9TyWKkw%3D%3D)


