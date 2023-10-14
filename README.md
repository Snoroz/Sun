# Sun

A simple dynamic lighting script that only displays shadows within a certain radius of the target.

# Requirements

This script requires the Ursina library.

```
pip install https://github.com/pokepetter/ursina/archive/master.zip --upgrade --force-reinstall
```

# How to use it

Import the Sun class and call it in your script, passing it the target as an argument (which is usually the player).

```python
# Import libraries
from ursina import *
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader

# Ursina class definition
app = Ursina(title = 'Sun', borderless = False)

from sun import Sun
import random as ra

# World
plane = Entity(model = 'plane', texture = 'grass', scale = 220, shader = lit_with_shadows_shader)
cube = Entity(model = 'cube', texture = 'white_cube', position = (0, 1.5, 0), scale = 3, color = color.red)
for i in range(15):
    sphere = Entity(model = 'sphere', texture = 'brick', position = (ra.randint(-100, 100), 3, ra.randint(-100, 100)), scale = 5)


# Use the arrow keys to move the cube.
def update():
    cube.x -= held_keys['left arrow'] * 30 * time.dt
    cube.x += held_keys['right arrow'] * 30 * time.dt
    cube.z -= held_keys['down arrow'] * 30 * time.dt
    cube.z += held_keys['up arrow'] * 30 * time.dt

# Light
sun = Sun(target = cube)

Sky()

EditorCamera()

app.run()
```
