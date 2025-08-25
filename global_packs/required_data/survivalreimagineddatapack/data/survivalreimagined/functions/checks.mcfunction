# Add the setup objective
scoreboard objectives add world_border_setup dummy
# Disable dayLightCycle
gamerule doDaylightCycle false
gamerule doDaylightCycle_tc false
gamerule doWeatherCycle false
# Give effects
effect give @a slowness infinite 49 true
effect give @a blindness infinite 0 true
effect give @a jump_boost infinite 128 true
effect give @a resistance infinite 4 true

# Check if there are enough logs in the spawn area
execute store result score WORLD_BORDER_LOGS world_border_setup run clone ~-10 ~-12 ~-10 ~10 ~8 ~10 ~-10 ~-12 ~-10 filtered #minecraft:logs force

# If there aren't, spread the player
execute if score WORLD_BORDER_LOGS world_border_setup matches ..6 run function survivalreimagined:spread
# And stop the function
execute if score WORLD_BORDER_LOGS world_border_setup matches ..6 run return 0

# Check if there's enough gravel in the spawn area
execute store result score WORLD_BORDER_GRAVEL world_border_setup run clone ~-8 ~-16 ~-8 ~8 ~12 ~8 ~-8 ~-16 ~-8 filtered minecraft:gravel force
tellraw @a [{"score":{"name":"WORLD_BORDER_GRAVEL","objective":"world_border_setup"}},{"text":" gravel"}]
# If there is 15 or more gravel, complete the setup
execute if score WORLD_BORDER_GRAVEL world_border_setup matches 15.. run function survivalreimagined:success
execute if score WORLD_BORDER_GRAVEL world_border_setup matches 15.. run return 0

# If there's less than 15 gravel, try placing it
execute if score WORLD_BORDER_GRAVEL world_border_setup matches ..14 store success score WORLD_BORDER_GRAVEL world_border_setup run place feature ore_gravel ~ ~-16 ~
tellraw @a [{"score":{"name":"WORLD_BORDER_GRAVEL","objective":"world_border_setup"}},{"text":" gravel"}]

# If gravel placing succeded complete the setup
execute if score WORLD_BORDER_GRAVEL world_border_setup matches 1.. run function survivalreimagined:success

# If the placing has failed, spread the player
execute if score WORLD_BORDER_GRAVEL world_border_setup matches 0 run function survivalreimagined:spread