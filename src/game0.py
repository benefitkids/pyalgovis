import pygamejr

ball = pygamejr.CircleSprite()
bee = pygamejr.ImageSprite(pygamejr.resources.image.bee)
bee.rect.top = 100

for frame in pygamejr.every_frame():
    ball.rect.x += 1
    bee.rect.x += 1
    ball.draw()
    bee.draw()
