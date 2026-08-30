# Runs the initial border setup only the first time the data pack is activated in this world
execute unless score $wbe_init wbe_data matches 1 run gamerule doDaylightCycle false
execute unless score $wbe_init wbe_data matches 1 run effect give @a minecraft:slowness infinite 49 true
execute unless score $wbe_init wbe_data matches 1 run effect give @a minecraft:blindness infinite 0 true
execute unless score $wbe_init wbe_data matches 1 run tellraw @a [{"text":"[World Border] ","color":"gold"},{"text":"Looking for a spawn point with nearby logs, please wait...","color":"yellow"}]
execute unless score $wbe_init wbe_data matches 1 at @p run function worldborder_expansion:find_spawn
