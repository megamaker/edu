#!/usr/bin/env python
#encoding=utf-8


from mcpi import minecraft

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()
mc.player.setPos(x, y + 100, z)
