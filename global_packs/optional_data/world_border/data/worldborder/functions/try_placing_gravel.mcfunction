tellraw @a [{"text": "Trying to place gravel"}]
execute store success score WORLD_BORDER_GRAVEL wb_setup run place feature ore_gravel ~ ~-20 ~
execute if score WORLD_BORDER_GRAVEL wb_setup matches 0 run tellraw @a [{"text": "Trying to place gravel 2"}]
execute if score WORLD_BORDER_GRAVEL wb_setup matches 0 store success score WORLD_BORDER_GRAVEL wb_setup run place feature ore_gravel ~-5 ~-20 ~-5
execute if score WORLD_BORDER_GRAVEL wb_setup matches 0 run tellraw @a [{"text": "Trying to place gravel 3"}]
execute if score WORLD_BORDER_GRAVEL wb_setup matches 0 store success score WORLD_BORDER_GRAVEL wb_setup run place feature ore_gravel ~5 ~-20 ~5
execute if score WORLD_BORDER_GRAVEL wb_setup matches 0 run tellraw @a [{"text": "Trying to place gravel 4"}]
execute if score WORLD_BORDER_GRAVEL wb_setup matches 0 store success score WORLD_BORDER_GRAVEL wb_setup run place feature ore_gravel ~-5 ~-20 ~5
execute if score WORLD_BORDER_GRAVEL wb_setup matches 0 run tellraw @a [{"text": "Trying to place gravel 5"}]
execute if score WORLD_BORDER_GRAVEL wb_setup matches 0 store success score WORLD_BORDER_GRAVEL wb_setup run place feature ore_gravel ~5 ~-20 ~-5

execute if score WORLD_BORDER_GRAVEL wb_setup matches 1.. run tellraw @a {"text": "Found good spawn, good luck", "color": "#FFD700", "bold": true}
execute if score WORLD_BORDER_GRAVEL wb_setup matches 1.. run tellraw @a {"text": "Due to a glitch in commands, I recommend to re-join the world/server.", "color": "#FF0000"}
execute if score WORLD_BORDER_GRAVEL wb_setup matches 1.. run function worldborder:actual_setup
execute if score WORLD_BORDER_GRAVEL wb_setup matches 0 run tellraw @a {"text": "Failed to place gravel, will try again in 5 seconds"}
execute if score WORLD_BORDER_GRAVEL wb_setup matches 0 run function worldborder:spread
execute if score WORLD_BORDER_GRAVEL wb_setup matches 0 run schedule function worldborder:try_setup 10t