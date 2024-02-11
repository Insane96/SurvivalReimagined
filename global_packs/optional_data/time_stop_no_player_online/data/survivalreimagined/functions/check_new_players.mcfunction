execute as @a[tag=!new_player_check] run tellraw @s [{"text":"Welcome to the Survival Reimagined Test server"}]
execute as @a[tag=!new_player_check] run tellraw @a [{"text":"The time has been set to day due to a new player joining"}]
execute as @a[tag=!new_player_check] run time set 0
execute as @a[tag=!new_player_check] run weather clear
tag @a[tag=!new_player_check] add new_player_check
schedule function survivalreimagined:check_new_players 1s