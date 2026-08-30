worldborder center ~ ~
worldborder set 15
worldborder warning distance 0
worldborder warning time 0
gamerule spawnRadius 0
gamerule insanesurvivaloverhaul:death_min_health 10
gamerule doDaylightCycle true
setworldspawn ~ ~ ~
tp @a ~ ~ ~
effect clear @a
give @a minecraft:torch 1
scoreboard players set $wbe_init wbe_data 1
tellraw @a [{"text":"[World Border] ","color":"gold"},{"text":"Spawn found! Border set to 15 blocks. It will expand by 2 blocks at dawn and dusk.","color":"green"}]
