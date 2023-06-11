# Sun

A simple dynamic lighting script.

# Requirements

This script requires the Ursina library.

```
pip install https://github.com/pokepetter/ursina/archive/master.zip --upgrade --force-reinstall
```

# How to use it

In an example script like this, all you have to do is import the Sun class and call it in your script, passing it the target as an argument (which is usually the player).

```
# Import libraries
from ursina import *
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader

# Ursina class definition
app = Ursina(title = 'Sun', borderless = False)

from sun import Sun

# World
plane = Entity(model = 'plane', texture = 'grass', scale = 20, shader = lit_with_shadows_shader)
cube = Entity(model = 'cube', texture = 'white_cube', position = (-1, 1, 0))
sphere = Entity(model = 'sphere', texture = 'brick', position = (1, 1, 0))


# Use the arrow keys to move the cube.
def update():
    cube.x += held_keys['right arrow'] * 4 * time.dt
    cube.x -= held_keys['left arrow'] * 4 * time.dt

# Light
sun = Sun(target = cube)

Sky()

EditorCamera()

app.run()
```

![screenshot](https://github.com/Snoroz/Sun/assets/55320908/b5ba0d08-43ee-4b63-b4da-d4f474ded3e7)
