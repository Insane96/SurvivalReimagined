effect give @a slowness infinite 49 true
effect give @a blindness infinite 0 true

# Check if there are enough logs in the spawn area
execute store result score WORLD_BORDER_LOGS world_border_setup run clone ~-3 ~-12 ~-3 ~3 ~8 ~3 ~-3 ~-12 ~-3 filtered #logs force
# If there aren't, spread the player
execute if score WORLD_BORDER_LOGS world_border_setup matches ..4 run function worldborder:spread
# Stop executing stuff
execute if score WORLD_BORDER_LOGS world_border_setup matches ..4 run return 0
# Change the above two lines to the one below in 1.20.2
# execute if score WORLD_BORDER_LOGS world_border_setup matches ..4 run return run function worldborder:new_spawn

# Else try check for gravel
execute if score WORLD_BORDER_LOGS world_border_setup matches 5.. run tellraw @a {"text": "Found good spawn, good luck", "color": "#FFD700", "bold": true}
execute as @p if score WORLD_BORDER_LOGS world_border_setup matches 5.. run function worldborder:actual_setup