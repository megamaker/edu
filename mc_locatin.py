#!/usr/bin/env python
#encoding=utf-8


from mcpi import minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
print pos.x, pos.y, pos.z

#x, y, z = mc.player.getPos()
#print pos.x, pos.y, pos.z
