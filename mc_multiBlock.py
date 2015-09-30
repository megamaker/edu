#!/usr/bin/env python
#encoding=utf-8


from mcpi import minecraft

mc = minecraft.Minecraft.create()

stone = 1
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, stone)
