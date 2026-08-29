# Esegue l'impostazione iniziale del border solo la prima volta che il data pack viene attivato in questo mondo
execute unless score $wbe_init wbe_data matches 1 run worldborder set 15
execute unless score $wbe_init wbe_data matches 1 at @p run worldborder center ~ ~
execute unless score $wbe_init wbe_data matches 1 run worldborder warning distance 0
execute unless score $wbe_init wbe_data matches 1 run worldborder warning time 0
execute unless score $wbe_init wbe_data matches 1 run gamerule insanesurvivaloverhaul:death_min_health 10
execute unless score $wbe_init wbe_data matches 1 run scoreboard players set $wbe_init wbe_data 1
execute unless score $wbe_init wbe_data matches 1 run tellraw @a [{"text":"[World Border] ","color":"gold"},{"text":"Confine impostato a 15 blocchi. Si espanderà di 2 blocchi ogni giorno.","color":"yellow"}]
