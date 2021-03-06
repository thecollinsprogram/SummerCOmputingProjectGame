#!/usr/bin/python3

# Represents a power up for the game.
# By BEN COLLINS

from canvas.canvas import *
from consts import *
from random import *
import time

class PowerUp:

	def __init__(self, game):
		self.game = game

		# Calculate a random starting position of the power up.
		x = (random() * 2 - 1) * MAP_SIZE
		y = (random() * 2 - 1) * MAP_SIZE

		# Create the power up's shape object and add it to the canvas.
		self.shape = Rect(x, y, POWERUP_SIZE, POWERUP_SIZE, POWERUP_COLORA, layer = "content")
		self.game.canvas.add(self.shape)

		self.color_change = time.time() + BLINK_DURATION

	def update(self, player):
		# Every so often make the power up get larger and change color.
		if time.time() > self.color_change:
			self.color_change += BLINK_DURATION
			if self.shape.color == POWERUP_COLORA:
				self.shape.color = POWERUP_COLORB
				self.shape.w = POWERUP_SIZE
				self.shape.h = POWERUP_SIZE
			else:
				self.shape.color = POWERUP_COLORA
				self.shape.w = POWERUP_BLINK_SIZE
				self.shape.h = POWERUP_BLINK_SIZE

		# Test for collision with every bullet and if one hits change hit to true and break.
		hit = False
		for bullet in player.bullets:
			xcheck = abs(self.shape.x - bullet.shape.x) * 2 < BULLET_SIZE + POWERUP_BLINK_SIZE
			ycheck = abs(self.shape.y - bullet.shape.y) * 2 < BULLET_SIZE + POWERUP_BLINK_SIZE
			if xcheck and ycheck:
				hit = True
				break
		
		# If hit give the power up a new random position and increase the players health to the restore point.
		if hit:
			self.shape.x = (random() * 2 - 1) * MAP_SIZE
			self.shape.y = (random() * 2 - 1) * MAP_SIZE
			player.health_green.w = player.health_yellow.w