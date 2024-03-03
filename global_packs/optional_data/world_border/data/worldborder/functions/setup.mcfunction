effect give @a slowness infinite 49 true
effect give @a blindness infinite 0 true

# Check if there are enough logs in the spawn area
execute store result score WORLD_BORDER_LOGS world_border_setup run clone ~-4 ~-12 ~-4 ~4 ~8 ~4 ~-4 ~-12 ~-4 filtered #logs force
# If there aren't, spread the player
execute if score WORLD_BORDER_LOGS world_border_setup matches ..6 run function worldborder:spread
# Stop executing stuff
execute if score WORLD_BORDER_LOGS world_border_setup matches ..6 run return 0
# Change the above two lines to the one below in 1.20.2
# execute if score WORLD_BORDER_LOGS world_border_setup matches ..4 run return run function worldborder:new_spawn

execute if score WORLD_BORDER_LOGS world_border_setup matches 7.. store success score WORLD_BORDER_GRAVEL world_border_setup run place feature ore_gravel ~ ~-12 ~

execute if score WORLD_BORDER_GRAVEL world_border_setup matches 1.. run tellraw @a {"text": "Found good spawn, good luck", "color": "#FFD700", "bold": true}
execute if score WORLD_BORDER_GRAVEL world_border_setup matches 1.. run tellraw @a {"text": "Due to a glitch in commands, I recommend to re-join the world/server.", "color": "#FF0000"}
execute if score WORLD_BORDER_GRAVEL world_border_setup matches 1.. run function worldborder:actual_setup
# tellraw @a [{"score": {"name": "WORLD_BORDER_GRAVEL", "objective": "world_border_setup"}}, {"text": " gravel"}]
execute if score WORLD_BORDER_GRAVEL world_border_setup matches 0 run function worldborder:spread