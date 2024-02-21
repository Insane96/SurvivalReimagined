worldborder center ~ ~ 
worldborder set 9 0
worldborder warning distance 0
gamerule spawnRadius 0
setworldspawn ~ ~ ~
setblock ~ ~-1 ~ minecraft:grass_block
setblock ~ ~ ~ minecraft:torch
execute store result score WORLD_BORDER world_border_setup run worldborder get
worldborder damage amount 1
worldborder damage buffer 1
time set 11
gamerule doDaylightCycle true
gamerule doImmediateRespawn true
effect clear @a
tp @a @s
gamerule iguanatweaks:doLooseRespawn false
gamerule iguanatweaks:deathGrave false