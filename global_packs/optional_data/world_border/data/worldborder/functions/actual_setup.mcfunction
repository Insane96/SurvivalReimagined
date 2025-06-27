worldborder center ~ ~ 
worldborder set 9 0
worldborder warning distance 0
gamerule spawnRadius 0
setworldspawn ~ ~ ~
setblock ~ ~-1 ~ minecraft:grass_block
setblock ~ ~ ~ minecraft:torch
execute store result score WORLD_BORDER wb_setup run worldborder get
worldborder damage amount 1
worldborder damage buffer 1
time set 0
gamerule doDaylightCycle true
effect clear @a
tp @a @s
gamerule iguanatweaks:doLooseRespawn false
gamerule iguanatweaks:deathGrave false

function worldborder:expand