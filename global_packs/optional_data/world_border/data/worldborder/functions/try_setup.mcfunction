execute as @p at @s unless score WORLD_BORDER world_border_setup matches 1.. run gamerule doDaylightCycle false
execute as @p at @s unless score WORLD_BORDER world_border_setup matches 1.. run gamerule doDaylightCycle_tc false
execute as @p at @s unless score WORLD_BORDER world_border_setup matches 1.. run function worldborder:setup