effect give @a slowness infinite 49 true
effect give @a blindness infinite 0 true

tellraw @a [{"text": "Checking for logs"}]
# Check if there are enough logs in the spawn area
execute store result score WORLD_BORDER_LOGS wb_setup run clone ~-6 ~-12 ~-6 ~6 ~8 ~6 ~-6 ~-12 ~-6 filtered #logs force
# If there aren't, spread the player
execute if score WORLD_BORDER_LOGS wb_setup matches ..6 run function worldborder:spread
# Stop executing stuff
execute if score WORLD_BORDER_LOGS wb_setup matches ..6 run return 0
# Change the above two lines to the one below in 1.20.2
# execute if score WORLD_BORDER_LOGS wb_setup matches ..6 run return run function worldborder:new_spawn

function worldborder:try_placing_gravel