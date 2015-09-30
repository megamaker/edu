#!/usr/bin/env python
#encoding=utf-8


from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

grass = 2
flower = 38

while True:
	x, y, z = mc.player.getPos()

	block_beneath = mc.getBlock(x, y - 1, z)

	if block_beneath == grass:
		mc.setBlock(x, y, z, flower)
	sleep(0.1)
